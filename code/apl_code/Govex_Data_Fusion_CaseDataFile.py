import pandas as pd
import geopandas as gpd
pd.options.display.max_columns=100
import requests
import io

#data from github jhu,import the lastest data from timeseries
df_Counties_confirmed=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
df_Counties_deaths=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

#check the latest date
tdst=df_Counties_confirmed.columns[-1]

# replace data with NY data
df_NY_confirmed_url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/NY%20Boroughs_Confirmed.csv"
download = requests.get(df_NY_confirmed_url).content
df_NY_confirmed = pd.read_csv(io.StringIO(download.decode('utf-8')))

df_NY_deaths_url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/NY%20Boroughs_Deaths.csv"
download = requests.get(df_NY_deaths_url).content
df_NY_deaths = pd.read_csv(io.StringIO(download.decode('utf-8')))

#skip the first column
df_NY_confirmed=df_NY_confirmed.iloc[:,1:]
df_NY_deaths=df_NY_deaths.iloc[:,1:]

#import NY data https://github.com/nychealth/coronavirus-data/blob/master/by-boro.csv
df_NY_new_url = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-boro.csv"
download = requests.get(df_NY_new_url).content
df_NY_new = pd.read_csv(io.StringIO(download.decode('utf-8')))

#get the latest case and death count for NYC boroughs
df_NY_confirmed[tdst]=df_NY_new['CASE_COUNT']
df_NY_deaths[tdst]=df_NY_new['DEATH_COUNT']

# replace with NY boroughs files
dates_list = df_NY_confirmed.columns[4:]
print(dates_list)

# df_NY_deaths=pd.read_csv(r'C:\Work_GovEx\COVID-19\Daily Data\JHU US Map_NY_KC_Duke_Nantucket Counties - Deaths.csv')
for days in dates_list:
    # print (days)
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS == df_NY_confirmed.iloc[0, 0], days] = df_NY_confirmed.loc[0][
        days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS == df_NY_confirmed.iloc[1, 0], days] = df_NY_confirmed.loc[1][
        days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS == df_NY_confirmed.iloc[2, 0], days] = df_NY_confirmed.loc[2][
        days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS == df_NY_confirmed.iloc[3, 0], days] = df_NY_confirmed.loc[3][
        days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS == df_NY_confirmed.iloc[4, 0], days] = df_NY_confirmed.loc[4][
        days]

    df_Counties_deaths.loc[df_Counties_deaths.FIPS == df_NY_deaths.iloc[0, 0], days] = df_NY_deaths.loc[0][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS == df_NY_deaths.iloc[1, 0], days] = df_NY_deaths.loc[1][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS == df_NY_deaths.iloc[2, 0], days] = df_NY_deaths.loc[2][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS == df_NY_deaths.iloc[3, 0], days] = df_NY_deaths.loc[3][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS == df_NY_deaths.iloc[4, 0], days] = df_NY_deaths.loc[4][days]

#deaths data has an extra column
df_Counties_deaths.drop(columns=['iso2'],inplace=True)


# convert table
def converttable(df):
    cols = df.columns.tolist()
    pd_list = []
    for i in range(11, df.shape[1]):
        temp_cols = cols[:11]
        temp_cols.append(cols[i])

        temp_pd = df[temp_cols].copy()
        temp_pd['dt'] = cols[i]
        temp_pd.rename(columns={cols[i]: 'value'}, inplace=True)
        pd_list.append(temp_pd)
    df_new = pd.concat(pd_list, axis=0, ignore_index=True)
    return df_new

df_confirmed_new = converttable(df_Counties_confirmed)
df_deaths_new = converttable(df_Counties_deaths)

#merge confirmed and deaths data
df_confirmed_new['dt']=pd.to_datetime(df_confirmed_new['dt'])
df_deaths_new['dt']=pd.to_datetime(df_deaths_new['dt'])
# Rename cols
df_confirmed_new.rename(columns = {'value': 'confirmed'}, inplace = True)
df_deaths_new.rename(columns = {'value': 'deaths'}, inplace = True)
# Merge two tables
df_merged = df_confirmed_new.merge(df_deaths_new[['Admin2','Province_State', 'Country_Region', 'dt', 'deaths','Population']],
                                   on = ['Admin2','Province_State', 'dt'],
                                   how = 'inner')
df_merged = df_merged[['Admin2','Province_State', 'FIPS', 'dt', 'confirmed', 'deaths','Population']]
df_merged['FIPS']=df_merged['FIPS'].fillna(0).astype(int)
df_merged['FIPS'] = df_merged['FIPS'].apply(lambda x: '{0:0>5}'.format(x))

#merge with shpfiles for geometry info
US_Counties_file = "/govex/COVID-19/data_tables/Data_for_UScounty_map/JHUCounties.shp"
US_Counties=gpd.read_file(US_Counties_file)
df_merged1=pd.merge(df_merged,US_Counties,how='left',left_on='FIPS',right_on='GEOID')

#select columns and rename
df_merged1 = df_merged1[['Admin2','Province_State', 'FIPS','ST_ID','dt', 'confirmed', 'deaths','Population']]
df_merged1.rename(columns={'Admin2':'Countyname','Province_State':'ST_Name','ST_ID':'ST_ID','confirmed':'Confirmed','deaths':'Deaths'},inplace=True)
#Format FIPS
df_merged1['FIPS']=df_merged1['FIPS'].fillna(0).astype(int)
df_merged1['FIPS'] = df_merged1['FIPS'].apply(lambda x: '{0:0>5}'.format(x))
#calculate IncidenceRate
df_merged1['IncidenceRate']=df_merged1['Confirmed']/df_merged1['Population']*100000
df_merged1['IncidenceRate']=df_merged1['IncidenceRate'].round(2)

#calculate new cases

# Sort values
df_merged1.sort_values(by = ['ST_Name','FIPS', 'dt'], ascending = True, inplace = True)

# Differences
df_merged1['NewCases'] = df_merged1.groupby(by = ['FIPS']).Confirmed.diff()

df_merged1['dt']=pd.to_datetime(df_merged1['dt']).dt.date
from datetime import date
df_merged1[df_merged1['dt']==date(2020,1,24)].head()

df_merged1.to_csv('df_Counties2020.csv')


