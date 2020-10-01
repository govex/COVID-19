# **************************** UNCLASSIFIED ****************************
# Copyright (C) 2020 Johns Hopkins University Applied Physics Laboratory
# 
# All Rights Reserved.
# This material may only be used, modified, or reproduced by or for the
# U.S. government persuant to the license rights granted under FAR
# clause 52.227-14 or DFARS clauses 252.227-7013/7014.
# For any other permission, please contact the Legal Office at JHU/APL.
# **********************************************************************

import pandas as pd
import numpy as np
import us

from HammingSmoother import HammingSmoother
from HelperFunctions import correct_and_smooth
import config

# Import confirmed case data
confirmed_cases_url = ''
if config.CONFIRMED_CASES_SOURCE == 'US':
    confirmed_cases_url = config.CONFIRMED_CASES_US_URL
elif config.CONFIRMED_CASES_SOURCE == 'global':
    confirmed_cases_url = config.CONFIRMED_CASES_GLOBAL_URL
else:
    print("Data source not recognized. Designate data source as 'US' or 'global' in the config file.")

confirmed_cases_raw = pd.read_csv(confirmed_cases_url)

# Assign this based on user specified options
confirmed_cases_aggregated = []

if config.AGGREGATE_BY_PROVINCE_STATE:

    if 'Province_State' in confirmed_cases_raw:
        column_aggregation_functions = {
            'iso2': 'first',
            'iso3': 'first',
            'code3': 'first',
            'Province_State': 'first',
            'Country_Region': 'first',
        }
        for date in confirmed_cases_raw.loc[:, '1/22/20':].columns.tolist():
            column_aggregation_functions[date] = 'sum'

        confirmed_cases_aggregated = confirmed_cases_raw.groupby('Province_State').agg(column_aggregation_functions)

    elif 'Province/State' in confirmed_cases_raw:
        column_aggregation_functions = {
            'Province/State': 'first',
            'Country/Region': 'first',
        }
        for date in confirmed_cases_raw.loc[:, '1/22/20':].columns.tolist():
            column_aggregation_functions[date] = 'sum'

        confirmed_cases_aggregated = confirmed_cases_raw.groupby('Province/State').agg(column_aggregation_functions)

    else:
        print("No Province_State or Province/State column found. Data will not be aggregated.")

elif config.AGGREGATE_BY_COUNTRY_REGION:

    if 'Country_Region' in confirmed_cases_raw:
        column_aggregation_functions = {
            'iso2': 'first',
            'iso3': 'first',
            'code3': 'first',
            'Country_Region': 'first',
        }
        for date in confirmed_cases_raw.loc[:, '1/22/20':].columns.tolist():
            column_aggregation_functions[date] = 'sum'

        confirmed_cases_aggregated = confirmed_cases_raw.groupby('Country_Region').agg(column_aggregation_functions)

    elif 'Country/Region' in confirmed_cases_raw:
        column_aggregation_functions = {
            'Country/Region': 'first',
        }
        for date in confirmed_cases_raw.loc[:, '1/22/20':].columns.tolist():
            column_aggregation_functions[date] = 'sum'

        confirmed_cases_aggregated = confirmed_cases_raw.groupby('Country/Region').agg(column_aggregation_functions)

    else:
        print("No Country_Region or Country/Region column found. Data will not be aggregated.")

else: 
    confirmed_cases_aggregated = confirmed_cases_raw

# Split confirmed cases into metadata and numbers
confirmed_cases_metadata = confirmed_cases_aggregated.loc[:, :'1/22/20']
confirmed_cases_metadata = confirmed_cases_metadata.iloc[:, :-1]
confirmed_cases_numbers = confirmed_cases_aggregated.loc[:, '1/22/20':]

# Handle testing data
if config.INCLUDE_STATE_TESTING_DATA:

    # Get testing data
    testing_raw = pd.read_csv(config.TESTING_URL)
    testing_raw = testing_raw[['date', 'state', 'totalTestResults']]

    # Pivot the table to match the format of the confirmed case data
    testing_numbers = testing_raw.pivot_table(index=['state'], columns=['date'], values='totalTestResults').fillna(0)
    
# Generate Hamming Smoother
try:
    smoother = HammingSmoother(config.HAMMING_SMOOTHER_WIDTH)
except Exception as e:
    raise

# Iterate through the rows of confirmed case data
# Correct and smooth data
# Calculate the mitigation score from the smoothed data
mitigation_scores = []
for index, row in confirmed_cases_numbers.iterrows():
    if (row == 0).all():
        mitigation_scores.append('')
    else:
        try:

            smoothed_confirmed_cases_deltas = correct_and_smooth(row, smoother)
            
            if config.INCLUDE_STATE_TESTING_DATA:
                state_abbreviation = us.states.lookup(index).abbr
                smoothed_testing_deltas = correct_and_smooth(testing_numbers.loc[state_abbreviation], smoother)
                smoothed_testing_deltas = list(map(lambda x: 0.5 if x < 0.5 else x, smoothed_testing_deltas))
                deltas = [ confirmed_cases / tests for confirmed_cases,tests in zip(smoothed_confirmed_cases_deltas, smoothed_testing_deltas)]
            else:
                deltas = smoothed_confirmed_cases_deltas

            try:
                if config.HORIZON == 0:
                    h_deltas = deltas
                else:
                    h_deltas = deltas[-config.HORIZON:]
            except Exception as e:
                print("\nHorizon must be an int >= 0\n")
                raise
        
            # Calculate the mitigation score
            if max(h_deltas) == 0:
                mitigation_score = 0
            else:
                mitigation_score = h_deltas[-1] / max(h_deltas) 

            # Add mitigation score to the dataframe
            mitigation_scores.append(mitigation_score)

        except Exception as e:
            print("No testing data available for " + index + ".")
            print(e)
            confirmed_cases_metadata = confirmed_cases_metadata.drop(index=index)

confirmed_cases_metadata['Mitigation_Score'] = mitigation_scores
confirmed_cases_metadata.to_csv(config.OUTPUT_FILENAME, index=False)
print("Output CSV file: " + config.OUTPUT_FILENAME)