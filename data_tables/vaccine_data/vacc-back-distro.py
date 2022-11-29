import os
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# TODO SHould use lookup table
state_abbr_dict = {"Alabama": "AL",
                   "Alaska": "AK"}

def back_distro_owid():
    # Date ranges to back distribute
    dates_to_change = [
        "2022-11-17",
        "2022-11-18",
        "2022-11-19",
        "2022-11-20",
        "2022-11-21",
        "2022-11-22",
    ]

    # Get the latest OWID vaccination data
    owid_data = pd.read_csv(
        "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
    )

    # Get list of all iso codes
    iso_codes = np.unique((owid_data["iso_code"].values).astype(str))

    # Change date column solely for comparison and retrieval
    owid_data["date"] = pd.to_datetime(owid_data["date"])

    # Check if there is a corresponding row for a specified date
    for date in dates_to_change:

        date_time = datetime.strptime(date, "%Y-%m-%d")
        # Reporting is a one off. Per Emily:
        # 'we are technically one day behind, so what OWID reports as 11/16 we report as 11/17,
        # and what it reports as 11/21 we report as 11/22 '
        date_time = date_time - timedelta(days=1)

        for iso_code in iso_codes:
            oswid_row = owid_data.loc[
                (owid_data["iso_code"] == iso_code) & (owid_data["date"] == date_time)
            ]

            # If row does not exist for the date:
            # Check to see if data for the previous date exists.
            # If so, get the index of the last date, insert row with stale data from the previous date.
            if oswid_row.shape[0] == 0:
                previous_date_time = date_time - timedelta(days=1)
                oswid_previous_date_row = owid_data.loc[
                    (owid_data["iso_code"] == iso_code)
                    & (owid_data["date"] == previous_date_time)
                ]
                if oswid_previous_date_row.shape[0] > 0:
                    index_to_insert = float(
                        str(oswid_previous_date_row.index[0]) + ".5"
                    )

                    row_to_insert = oswid_previous_date_row.copy()
                    row_to_insert["date"] = date_time
                    row_to_insert = row_to_insert.values[0]

                    # Insert the data
                    owid_data.loc[index_to_insert] = row_to_insert
                    owid_data = owid_data.sort_index().reset_index(drop=True)

    owid_data["date"] = owid_data["date"].dt.strftime("%Y-%m-%d")
    owid_data.to_csv("owid-back-distro-vaccinations.csv", index=False)


def get_data_sets():
    # Dates to back distribute
    dates_to_change = [
        "2022-11-17",
        "2022-11-18",
        "2022-11-19",
        "2022-11-20",
        "2022-11-21",
        "2022-11-22",
    ]
    owid_data = pd.read_csv(
        os.path.dirname(__file__) + "/owid-back-distro-vaccinations.csv"
    )

    latest_vacc_doses_admin_global = pd.read_csv(
        "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_doses_admin_global.csv"
    )
    iso_codes = np.unique((latest_vacc_doses_admin_global["iso3"].values).astype(str))

    global_row_length = latest_vacc_doses_admin_global.shape[0]
    owid_data["date"] = pd.to_datetime(owid_data["date"])

    # For each date, retrieve the owid data for each iso code with the corresponding date
    for date in dates_to_change:
        default_column_array = [np.nan] * global_row_length
        date_time = datetime.strptime(date, "%Y-%m-%d")

        # Reporting is a one off. Per Emily:
        # 'we are technically one day behind, so what OWID reports as 11/16 we report as 11/17,
        # and what it reports as 11/21 we report as 11/22 '
        date_time = date_time - timedelta(days=1)
        for iso_code in iso_codes:
            oswid_row = owid_data.loc[
                (owid_data["iso_code"] == iso_code) & (owid_data["date"] == date_time)
            ]

            if oswid_row.shape[0] > 0:
                global_admin_row_index = latest_vacc_doses_admin_global.loc[
                    latest_vacc_doses_admin_global["iso3"] == iso_code
                ].index[0]
                oswid_value = oswid_row["total_vaccinations"].values[0]
                default_column_array[global_admin_row_index] = oswid_value

        latest_vacc_doses_admin_global[date] = default_column_array
    latest_vacc_doses_admin_global.to_csv(
        "test_time_series_covid19_vaccine_doses_admin_global2.csv", index=False
    )


def back_distribute_us_vaccine():
    dates_to_change = [
        "2022-11-17",
        "2022-11-18",
        "2022-11-19",
        "2022-11-20",
        "2022-11-21",
        "2022-11-22",
    ]

    # Location of CDC downloaded data from:
    # https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc/data
    cdc_data = pd.read_csv("/Users/weslejl1/Downloads/COVID-19_Vaccinations_in_the_United_States_Jurisdiction.csv")

    govex_us_data = pd.read_csv("https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/us_data/time_series/time_series_covid19_vaccine_doses_admin_US.csv")

    govex_row_length = govex_us_data.shape[0]

    # Iterate cdc dataset to create a new column for each date in the dates_to_change array.
    for date in dates_to_change:
        if date not in govex_us_data.columns:
            # Create empty column
            default_column_array = [np.nan] * govex_row_length
            govex_us_data[date] = default_column_array

            # Get the rows for a specific date. Data is stale for a week at a time.
            cdc_single_date_df = cdc_data.loc[
                (govex_us_data["Date"] == "11/16/2022")
                ]

            for ind, row in cdc_single_date_df.iterrows():
                # Add in the corresponding data from CDC based on the GOVEX index for each state
                state_abbreviation = row["Location"]
                state_full = state_abbr_dict[state_abbreviation]
                # Get the index needed to insert the corresponding CDC value
                govex_row_index = govex_us_data.loc[
                    (govex_us_data["Province_State"] == state_full)
                    ].index[0]

                cdc_value = row["Distribution"].value
                default_column_array[govex_row_index] = cdc_value


if __name__ == "__main__":
    back_distribute_us_vaccine()
