# This code is for generating the shapefiles for the GovEx US Covid Map

import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import geopandas as gpd
pd.options.display.max_columns=100
import requests
import io

#get confirmed data from github jhu,import the lastest data from timeseries
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df_Counties_confirmed = pd.read_csv(io.StringIO(download.decode('utf-8')))

#get the lastest date
tdst=df_Counties_confirmed.columns[-1]
print (tdst)

#extracting last 14 days from time series
Day14Series=[]
print(df_Counties_confirmed.columns)
for i in range(1,15):
    day=df_Counties_confirmed.columns[(i-16)]
    Day14Series.append(day)
len(Day14Series)
Day14Series.extend([tdst,'FIPS', 'Admin2','Province_State','Combined_Key'])
print(Day14Series)
df_Counties_confirmed=df_Counties_confirmed[Day14Series]

# replacing NYC data point with NYC borough data
df_NY_confirmed_url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/NY%20Boroughs_Confirmed.csv"
download = requests.get(df_NY_confirmed_url).content
df_NY_confirmed = pd.read_csv(io.StringIO(download.decode('utf-8')))

df_NY_deaths_url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/NY%20Boroughs_Deaths.csv"
download = requests.get(df_NY_deaths_url).content
df_NY_deaths = pd.read_csv(io.StringIO(download.decode('utf-8')))


df_NY_confirmed=df_NY_confirmed.iloc[:,1:]
df_NY_deaths=df_NY_deaths.iloc[:,1:]

# import NY data https://github.com/nychealth/coronavirus-data/blob/master/by-boro.csv
df_NY_new_url = "https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-boro.csv"
download = requests.get(df_NY_new_url).content
df_NY_new = pd.read_csv(io.StringIO(download.decode('utf-8')))

#get the latest case and death count for NYC boroughs
df_NY_confirmed[tdst]=df_NY_new['CASE_COUNT']
df_NY_deaths[tdst]=df_NY_new['DEATH_COUNT']

# creating last 14 day time series for NY data
for days in df_Counties_confirmed.columns[:15]:
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[0,0],days]=df_NY_confirmed.loc[0][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[1,0],days]=df_NY_confirmed.loc[1][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[2,0],days]=df_NY_confirmed.loc[2][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[3,0],days]=df_NY_confirmed.loc[3][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[4,0],days]=df_NY_confirmed.loc[4][days]

#calcualte new cases for 14 days
df_Counties_confirmed['NewCaseDay01']=df_Counties_confirmed.iloc[:,1]-df_Counties_confirmed.iloc[:,0]
df_Counties_confirmed['NewCaseDay02']=df_Counties_confirmed.iloc[:,2]-df_Counties_confirmed.iloc[:,1]
df_Counties_confirmed['NewCaseDay03']=df_Counties_confirmed.iloc[:,3]-df_Counties_confirmed.iloc[:,2]
df_Counties_confirmed['NewCaseDay04']=df_Counties_confirmed.iloc[:,4]-df_Counties_confirmed.iloc[:,3]
df_Counties_confirmed['NewCaseDay05']=df_Counties_confirmed.iloc[:,5]-df_Counties_confirmed.iloc[:,4]
df_Counties_confirmed['NewCaseDay06']=df_Counties_confirmed.iloc[:,6]-df_Counties_confirmed.iloc[:,5]
df_Counties_confirmed['NewCaseDay07']=df_Counties_confirmed.iloc[:,7]-df_Counties_confirmed.iloc[:,6]
df_Counties_confirmed['NewCaseDay08']=df_Counties_confirmed.iloc[:,8]-df_Counties_confirmed.iloc[:,7]
df_Counties_confirmed['NewCaseDay09']=df_Counties_confirmed.iloc[:,9]-df_Counties_confirmed.iloc[:,8]
df_Counties_confirmed['NewCaseDay10']=df_Counties_confirmed.iloc[:,10]-df_Counties_confirmed.iloc[:,9]
df_Counties_confirmed['NewCaseDay11']=df_Counties_confirmed.iloc[:,11]-df_Counties_confirmed.iloc[:,10]
df_Counties_confirmed['NewCaseDay12']=df_Counties_confirmed.iloc[:,12]-df_Counties_confirmed.iloc[:,11]
df_Counties_confirmed['NewCaseDay13']=df_Counties_confirmed.iloc[:,13]-df_Counties_confirmed.iloc[:,12]
df_Counties_confirmed['NewCases']=df_Counties_confirmed.iloc[:,14]-df_Counties_confirmed.iloc[:,13]

#get the confirmed data for the latest date and new cases data
df_Counties_confirmed=df_Counties_confirmed[df_Counties_confirmed.columns[-19:]]

#get deaths data from github jhu,import the lastest data from timeseries
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df_Counties_deaths = pd.read_csv(io.StringIO(download.decode('utf-8')))

#calculate new deaths
pre_day=df_Counties_deaths.columns[-2]
df_Counties_deaths=df_Counties_deaths[[pre_day,tdst,'FIPS']]

# updates death data with NYC deaths data
for days in df_Counties_deaths.columns[:2]:
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[0,0],days]=df_NY_deaths.loc[0][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[1,0],days]=df_NY_deaths.loc[1][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[2,0],days]=df_NY_deaths.loc[2][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[3,0],days]=df_NY_deaths.loc[3][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[4,0],days]=df_NY_deaths.loc[4][days]

# remove previous day data
df_Counties_deaths['NewDeaths']=df_Counties_deaths.iloc[:,1]-df_Counties_deaths.iloc[:,0]
df_Counties_deaths.drop(columns={pre_day},inplace=True)

# merge confirmed and deaths data
df_Counties=pd.merge(df_Counties_confirmed,df_Counties_deaths,how='left',on='FIPS',suffixes=('_confirmed','_deaths'))
df_Counties.rename(columns={tdst+'_confirmed':'Confirmed',tdst+'_deaths':'Deaths'},inplace=True)

# get ACS County and Definitive Health data
url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/ACSCounty_DefHealth_Data.csv"
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df_CountyHealth = pd.read_csv(io.StringIO(download.decode('utf-8')))

#Merge JHU data with Esri County data, left join to keep all the confirmed cases
df_Counties1=pd.merge(df_Counties,df_CountyHealth,how='left',left_on='FIPS',right_on='FIPS')

# get Population, Poverty, and Employent data
url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/Pop_Pov_Eco_Data.csv"
download = requests.get(url).content

# reading the downloaded content and turning it into a pandas dataframe
demo = pd.read_csv(io.StringIO(download.decode('utf-8')))

# merge JHU,Esri, Demo data
USCounties1=pd.merge(df_Counties1,demo,how='left',left_on='FIPS',right_on='FIPS')

# get daily report for state data
td=datetime.strftime(datetime.now()-timedelta(1), '%m-%d-%Y')

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
new_url = url+str(td)+".csv"
download = requests.get(new_url).content
df_new = pd.read_csv(io.StringIO(download.decode('utf-8')))

df_USnew=df_new[df_new['Country_Region']=='US']

dfStates=pd.pivot_table(df_USnew,values=['Confirmed', 'Deaths', 'Recovered',
       'Active'],index=['Province_State'],aggfunc=np.sum)

dfStates.rename(columns={'Confirmed':'State_Confirmed','Deaths':'State_Deaths','Recovered':'State_Recovered'},inplace=True)

dfStates.reset_index(inplace=True)

# merge UScounties1 with state data
USCounties2=pd.merge(USCounties1,dfStates,how='outer',left_on='State',right_on='Province_State')

# add Red Cross data
url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/Red%20Cross%20Centroids%20for%20COVID19%20Public%20Health%20Emergency%20Status%20by%20County_0.csv"
download = requests.get(url).content
dfRC = pd.read_csv(io.StringIO(download.decode('utf-8')))
dfRC1=dfRC[['FIPS','Notes','Last Update', 'Local Public Emergency']]
dfRC1.loc[dfRC1['Local Public Emergency']=='Red','Local Public Emergency']= 'Govt Ordered Community Quarantine'
dfRC1.loc[dfRC1['Local Public Emergency']=='Orange','Local Public Emergency']= 'Govt Directed Social Distancing'
dfRC1.loc[dfRC1['Local Public Emergency']=='Yellow','Local Public Emergency']= 'Declared Public Health Emergency'
dfRC1['Local Public Emergency'].unique()
dfRC1.rename(columns={'Notes':'EM_notes','Last Update':'EM_date','Local Public Emergency':'EM_type'},inplace=True)

#merge UScounties2 with Red Cross data
USCounties3=pd.merge(USCounties2, dfRC1,how='left',left_on='FIPS',right_on='FIPS')

#import US Counties, State shp file downloaded from Esri
US_Counties_file = "/govex/COVID-19/data_tables/Data_for_UScounty_map/JHUCounties.shp"
US_Counties=gpd.read_file(US_Counties_file)
US_Counties.rename(columns={'NAME':'Countyname','COUNTYFP':'CountyFP'},inplace=True)
US_Counties['GEOID']=US_Counties['GEOID'].astype(float)

#import state testing data from https://covidtracking.com/api/states
dfStatesTesting=pd.read_json('https://covidtracking.com/api/v1/states/current.json')
dfStatesTesting=dfStatesTesting[['state','total','dateChecked']]
dfStatesTesting.rename(columns={'total':'State_Testing','dateChecked':'DateChecked'},inplace=True)

#Merge with state testing data
USCounties=pd.merge(US_Counties,dfStatesTesting,how='left',left_on='ST_Abbr',right_on='state')

#Import Race data
url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/County_ShpHeaders.csv"
download = requests.get(url).content
Counties_race = pd.read_csv(io.StringIO(download.decode('utf-8')))

url = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/Data_for_UScounty_map/Race_Age.csv"
download = requests.get(url).content
Race_Age = pd.read_csv(io.StringIO(download.decode('utf-8')))

Race_Agemerge=pd.merge(Counties_race,Race_Age,how='left',left_on='GEOIDFIPS',right_on='FIPS')

USCountiesm1=pd.merge(USCounties,Race_Agemerge,how='left',left_on='GEOID',right_on='GEOIDFIPS')
USCountiesm1=USCountiesm1[['Countyname', 'GEOID', 'ST_Abbr', 'ST_ID', 'ST_Name', 'geometry',
       'state', 'State_Testing', 'DateChecked', 'ObjectID', 'CountyGNIS',
       'GEOIDFIPS', 'TotalPop',
       'NonHispWhPop',  'BlackPop',
      'AmIndop',  'AsianPop',
       'PacIslPop',  'OtherPop',  'TwoMorPop',
       'HispPop',  'PCPopNWh',
       'PCPopBk', 'PCPopAI', 'PCPopAs',
      'PPCPopPI',  'PCPopOr',
       'PCPopTm',  'PCPopHL',
       'racePop_total', 'White alone',
       'Black or African American alone',
       'American Indian and Alaska Native alone', 'Asian alone',
       'Native Hawaiian and Other Pacific Islander alone',
       'Some other race alone', 'Two or more races',
       'Not Hispanic or Latino origin', 'Hispanic or Latino Origin',
       'Age_under15', 'Age_15_24', 'Age_25_34', 'Age_35_64', 'Age_65_74',
       'Age_over75', 'Agetotal' ]]

#join the Countyshp and State testing file with USCounties3
USCounties4=pd.merge(USCountiesm1,USCounties3,how='right',left_on='GEOID',right_on='FIPS')
USCounties4.to_file('USCounties_JHUmap.shp')