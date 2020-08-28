from datetime import date
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import geopandas as gpd
from pathlib import Path
import re
import os

pd.options.display.max_columns = 100

# data from github jhu,import the lastest data from timeseries
df_Counties_confirmed = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
df_Counties_deaths = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")

# Root file variables -- to use a dynamic variable append set "COVID-19-ROOT" to the root path of this repository.
covid19Root = Path(os.getenv('COVID_19_ROOT', "~/Documents/GitHub/COVID-19")).expanduser()

print(f'COVID-19 Root Path is {covid19Root}')

covid19Data = covid19Root / "data_tables/Data_for_UScounty_map/"
covid19Export = covid19Root / "data_tables/JHU_USCountymap_TEST/"




# the lastest date, printing both just make sure they have the data are updated at the same pace
yesterday = '{d.month}/{d.day}/{d.year}'.format(
    d=datetime.now() - timedelta(days=1))

tdst = df_Counties_confirmed.columns[-1]
tdst1 = df_Counties_deaths.columns[-1]

if tdst and tdst1 == yesterday[:-4] + yesterday[-2:]:
    print("The Confirmed and Death tables are up to date")
else:
    print("Error: The Confirmed and Death tables are not up to date")



# Change date on yesterday's csv and zipped shapefile in TEST folder
oldZip = covid19Export / 'USCounties_JHUmap.zip'
oldCsv = covid19Export / 'df_Counties2020.csv'
zipDate = 'USCounties_JHUmap_' + tdst.replace("/", "-") + '.zip'
csvDate = 'df_Counties2020_' + tdst.replace("/", "-") + '.csv'

oldZip.rename(covid19Export / zipDate)
oldCsv.rename(covid19Export / csvDate)



# Exclude military and extra data added to the end
# df_Counties_confirmed=df_Counties_confirmed.iloc[:3251]
# df_Counties_deaths=df_Counties_deaths.iloc[:3251]
# #df_Counties_confirmed.iloc[-2:]



Day14Series=[]
for i in range(1,15):
    #print (i)
    day=df_Counties_confirmed.columns[(i-16)]
    Day14Series.append(day)
    
len(Day14Series)
Day14Series.extend([tdst,'FIPS', 'Admin2','Province_State','Combined_Key'])
df_Counties_confirmed=df_Counties_confirmed[Day14Series]



# Replace data with NY data
df_NY_confirmed=pd.read_csv( covid19Data / 'NY_Boroughs_Confirmed.csv')
df_NY_deaths=pd.read_csv( covid19Data / 'NY_Boroughs_Deaths.csv')
#skip the first column
df_NY_confirmed=df_NY_confirmed.iloc[:,1:]
df_NY_deaths=df_NY_deaths.iloc[:,1:]
#import NY data https://github.com/nychealth/coronavirus-data/blob/master/by-boro.csv
df_NY_new=pd.read_csv("https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-boro.csv",skipfooter=1,engine='python')



if tdst == df_NY_confirmed.columns[-1]:
    print ('Error: The New York data is not updated or has already been updated')
   # new_date='{dt.month}/{dt.day}/{dt:%y}'.format(dt = datetime.now())
   # new_date='{dt.month}/{dt.day}/{dt:%y}'.format(dt = datetime.now()-timedelta(1)
    #df_NY_confirmed[new_date]=df_NY_new['CASE_COUNT']
    #df_NY_deaths[new_date]=df_NY_new['DEATH_COUNT']
else:
    print ('The New York data is updated')
    df_NY_confirmed[tdst]=df_NY_new['CASE_COUNT']
    df_NY_deaths[tdst]=df_NY_new['DEATH_COUNT']
df_Counties_confirmed.columns


#15 days time-series
for days in df_Counties_confirmed.columns[:15]:
#     print (days)
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



#clean confirmed file
#df_Counties_confirmed.columns[-19:]
df_Counties_confirmed=df_Counties_confirmed[df_Counties_confirmed.columns[-19:]]



#calculate new deaths
pre_day=df_Counties_deaths.columns[-2]
df_Counties_deaths=df_Counties_deaths[[pre_day,tdst,'FIPS']]



for days in df_Counties_deaths.columns[:2]:
#     print (days)
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[0,0],days]=df_NY_deaths.loc[0][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[1,0],days]=df_NY_deaths.loc[1][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[2,0],days]=df_NY_deaths.loc[2][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[3,0],days]=df_NY_deaths.loc[3][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[4,0],days]=df_NY_deaths.loc[4][days]



df_Counties_deaths['NewDeaths']=df_Counties_deaths.iloc[:,1]-df_Counties_deaths.iloc[:,0]
df_Counties_deaths.drop(columns={pre_day},inplace=True)



#tdst=df_Counties_confirmed.columns[-1]

df_Counties=pd.merge(df_Counties_confirmed,df_Counties_deaths,how='left',on='FIPS',suffixes=('_confirmed','_deaths'))
#df_Counties.head(2)
df_Counties.rename(columns={tdst+'_confirmed':'Confirmed',tdst+'_deaths':'Deaths'},inplace=True) 



#census and health data from ESRI
df_ACS1=pd.read_excel( covid19Data / 'ACS_2014-2018_Fields.xlsx')
df_ACSState=pd.read_excel( covid19Data / 'ACS_State_Final_ToExcel_noMOE.xlsx')
df_ACSCounty=pd.read_excel( covid19Data / 'ACS_County_Final_ToExcel_noMOE.xlsx')
df_ACSCounty1=df_ACSCounty[['FIPS', 'NAME', 'State']]
df_ACSCounty1['Age_85']=df_ACSCounty['B01001_049E']+df_ACSCounty['B01001_025E']
df_ACSCounty1['Age_80_84']=df_ACSCounty['B01001_048E']+df_ACSCounty['B01001_024E']
df_ACSCounty1['Age_75_79']=df_ACSCounty['B01001_047E']+df_ACSCounty['B01001_023E']
df_ACSCounty1['Age_70_74']=df_ACSCounty['B01001_046E']+df_ACSCounty['B01001_022E']
df_ACSCounty1['Age_65_69']=df_ACSCounty['B01001_045E']+df_ACSCounty['B01001_021E']+df_ACSCounty['B01001_044E']+df_ACSCounty['B01001_020E']
df_ACSCounty1['AgedPop']=df_ACSCounty1['Age_85']+df_ACSCounty1['Age_80_84']+df_ACSCounty1['Age_75_79']+df_ACSCounty1['Age_70_74']+df_ACSCounty1['Age_65_69']
# df_ACSCounty1.head(2)



df_Healthcare=pd.read_excel( covid19Data / 'Definitive_Healthcare_Hospital_Beds_By_County_and_Demographics.xlsx',
                            sheet_name= 'Sheet2',skiprows=2)
df_Healthcare1=df_Healthcare[['Row Labels', 'Sum of NUM_LICENSED_BEDS', 'Sum of NUM_STAFFED_BEDS',
       'Sum of NUM_ICU_BEDS','Sum of AVG_VENTILATOR_USAGE']]
   #                           'ID','Sum # of Licensed Beds', 'Sum # of Staffed Beds', 'Sum # of ICU Beds','Average Average Ventilator Usage']]
df_Healthcare1.rename(columns={'Row Labels':'ID','Sum of NUM_LICENSED_BEDS':'Beds_Licensed','Sum of NUM_STAFFED_BEDS':'Beds_Staffed','Sum of NUM_ICU_BEDS':'Beds_ICU',
                             'Sum of AVG_VENTILATOR_USAGE':'Ventilators_Average' },inplace=True)
df_CountyHealth=pd.merge(df_ACSCounty1,df_Healthcare1,how='inner',left_on='FIPS',right_on='ID')
# df_CountyHealth.shape



#Merge JHU data with Esri County data, left join to keep all the confirmed cases
df_Counties1=pd.merge(df_Counties,df_CountyHealth,how='left',left_on='FIPS',right_on='FIPS') 



#import demographic info  https://data.census.gov/cedsci/  data source: https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/
df_pop=pd.read_excel(covid19Data / 'PopulationEstimates.xls',skiprows=2)
df_poverty=pd.read_excel(covid19Data / 'PovertyEstimates.xls',skiprows=4)
#df_edu=pd.read_excel(covid19Data / 'Education.xls',skiprows=4)
df_eco=pd.read_excel(covid19Data / 'employment.xls',skiprows=4)



df_eco=df_eco.drop(df_eco.index[0])
df_poverty=df_poverty.drop(df_poverty.index[0])
df_pop=df_pop.drop(df_pop.index[0])
#df_eco.head(2)



#Select columns from demo data
df_pop1=df_pop[['FIPS','POP_ESTIMATE_2018']]
df_poverty1=df_poverty[['FIPStxt','POVALL_2018','PCTPOVALL_2018']]
#df_edu1=df_edu[[]]
df_eco1=df_eco[['FIPS','Unemployed_2018','Unemployment_rate_2018','Median_Household_Income_2018','Med_HH_Income_Percent_of_State_Total_2018']]



#merge demo data
demo1=pd.merge(df_pop1,df_poverty1,how='left',left_on='FIPS',right_on='FIPStxt')
demo2=pd.merge(demo1,df_eco1,how='right',left_on='FIPS',right_on='FIPS')



#merge JHU,Esri, Demo data
USCounties1=pd.merge(df_Counties1,demo2,how='left',left_on='FIPS',right_on='FIPS')



#import the most recent daily data from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
td=datetime.strftime(datetime.now()-timedelta(1), '%m-%d-%Y')
#td=datetime.strftime(datetime.now(), '%m-%d-%Y')
# print (str(td))
#df_new=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+str(td)+".csv")
df_new=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"+str(td)+".csv")
df_USnew=df_new[df_new['Country_Region']=='US']
dfStates=pd.pivot_table(df_USnew,values=['Confirmed', 'Deaths', 'Recovered',
       'Active'],index=['Province_State'],aggfunc=np.sum)
dfStates.rename(columns={'Confirmed':'State_Confirmed','Deaths':'State_Deaths','Recovered':'State_Recovered'},inplace=True)
#dfStates['State_Testing']=999
dfStates.reset_index(inplace=True)
# dfStates.State_Recovered.sum()



#dfStates



#merge UScounties1 with state data
USCounties2=pd.merge(USCounties1,dfStates,how='outer',left_on='State',right_on='Province_State')


#import Red Cross
dfRC=pd.read_csv( covid19Data / 'Red_Cross_Centroids_for_COVID19_Public_Health_Emergency_Status_by_County_0.csv')



dfRC1=dfRC[['FIPS','Notes','Last Update', 'Local Public Emergency']]
dfRC1.loc[dfRC1['Local Public Emergency']=='Red','Local Public Emergency']= 'Govt Ordered Community Quarantine'
dfRC1.loc[dfRC1['Local Public Emergency']=='Orange','Local Public Emergency']= 'Govt Directed Social Distancing'
dfRC1.loc[dfRC1['Local Public Emergency']=='Yellow','Local Public Emergency']= 'Declared Public Health Emergency'



# dfRC1['Local Public Emergency'].unique()



dfRC1.rename(columns={'Notes':'EM_notes','Last Update':'EM_date','Local Public Emergency':'EM_type'},inplace=True)



#merge UScounties2 with RC data
USCounties3=pd.merge(USCounties2, dfRC1,how='left',left_on='FIPS',right_on='FIPS')



#import US Counties, State shp file downloaded from Esri
US_Counties=gpd.read_file( covid19Data / "JHUCounties.shp")
US_Counties.rename(columns={'NAME':'Countyname','COUNTYFP':'CountyFP'},inplace=True)
US_Counties['GEOID']=US_Counties['GEOID'].astype(float)



#import state testing data from https://covidtracking.com/api/states
dfStatesTesting=pd.read_json('https://covidtracking.com/api/v1/states/current.json')
dfStatesTesting=dfStatesTesting[['state','total','dateChecked']]
dfStatesTesting.rename(columns={'total':'State_Testing','dateChecked':'DateChecked'},inplace=True)



#Merge with state testing data
USCounties=pd.merge(US_Counties,dfStatesTesting,how='left',left_on='ST_Abbr',right_on='state')



#Import Race data
#USCounties_pre=gpd.read_file(r"C:\Work_GovEx\COVID-19\Daily Data\USCounties_JHUmap_05_05\USCounties_JHUmap.shp")
Counties_race=pd.read_csv( covid19Data / 'County_ShpHeaders.csv')
Race_Age=pd.read_csv( covid19Data / 'Race_Age.csv')



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
#USCounties1=pd.merge(US_Counties,df_USnew,how='left',left_on='forjoin',right_on='Combined_Key1')



#Add calcuations
USCounties4['FatalityRate']=USCounties4['Deaths']/USCounties4['Confirmed']*100
USCounties4['ConfirmedbyPop']=USCounties4['Confirmed']/USCounties4['POP_ESTIMATE_2018']*100000
USCounties4['DeathsbyPop']=USCounties4['Deaths']/USCounties4['POP_ESTIMATE_2018']*100000
USCounties4['State_FatalityRate']=USCounties4['State_Deaths']/USCounties4['State_Confirmed']*100
USCounties4['Recovered']=0  # place holder
USCounties4['Active']=0   #place holder
USCounties4['url']='infUrl' #place holder
USCounties4['Thumbnail']='placeholder' #place holder



USCounties4['ConfirmedbyPop']=USCounties4['ConfirmedbyPop'].round(2)



#select columns
USCounties4=USCounties4[['Admin2', 'Province_State_x','ST_Abbr', 'ST_ID',  'geometry',
       'FIPS', 'FatalityRate', 'ConfirmedbyPop','DeathsbyPop', 'PCTPOVALL_2018', 
         'Unemployment_rate_2018', 'Med_HH_Income_Percent_of_State_Total_2018',
       'State_FatalityRate', 'DateChecked',
        'EM_type', 'EM_date','EM_notes','url', 'Thumbnail', 'Confirmed',  'Deaths',
        'Age_85', 'Age_80_84', 'Age_75_79', 'Age_70_74', 'Age_65_69',  
        'Beds_Licensed', 'Beds_Staffed','Beds_ICU', 'Ventilators_Average', 
        'POP_ESTIMATE_2018','POVALL_2018', 'Unemployed_2018','Median_Household_Income_2018',
        'Recovered', 'Active', 'State_Confirmed', 'State_Deaths', 'State_Recovered',
       'State_Testing',  'AgedPop','NewCases','NewDeaths','TotalPop', 'NonHispWhPop', 'BlackPop', 'AmIndop',
       'AsianPop', 'PacIslPop', 'OtherPop', 'TwoMorPop', 'HispPop', 'PCPopNWh',
       'PCPopBk', 'PCPopAI', 'PCPopAs', 'PPCPopPI', 'PCPopOr', 'PCPopTm',
       'PCPopHL','racePop_total', 'White alone',
       'Black or African American alone',
       'American Indian and Alaska Native alone', 'Asian alone',
       'Native Hawaiian and Other Pacific Islander alone',
       'Some other race alone', 'Two or more races',
       'Not Hispanic or Latino origin', 'Hispanic or Latino Origin',
       'Age_under15', 'Age_15_24', 'Age_25_34', 'Age_35_64', 'Age_65_74',
       'Age_over75', 'Agetotal']]
USCounties4.rename(columns={'Admin2':'Countyname'},inplace=True)
USCounties4.rename(columns={'Province_State_x':'ST_Name'},inplace=True)



USCounties4['FIPS']=USCounties4['FIPS'].fillna(0).astype(int)
USCounties4['FIPS']=USCounties4['FIPS'].apply(str).str.pad(width=5, side='left', fillchar='0')
USCounties4['Age_85']=USCounties4['Age_85'].fillna(0).astype(int)
USCounties4['Age_80_84']=USCounties4['Age_80_84'].fillna(0).astype(int)
USCounties4['Age_75_79']=USCounties4['Age_75_79'].fillna(0).astype(int)
USCounties4['Age_70_74']=USCounties4['Age_70_74'].fillna(0).astype(int)
USCounties4['Age_65_69']=USCounties4['Age_65_69'].fillna(0).astype(int)
USCounties4['AgedPop']=USCounties4['AgedPop'].fillna(0).astype(int)
USCounties4['Beds_Licensed']=USCounties4['Beds_Licensed'].fillna(0).astype(int)
USCounties4['Beds_ICU']=USCounties4['Beds_ICU'].fillna(0).astype(int)
USCounties4['Beds_Staffed']=USCounties4['Beds_Staffed'].fillna(0).astype(int)
# USCounties4['NewCases']=USCounties4['NewCases'].fillna(0).astype(int)
# USCounties4['NewDeaths']=USCounties4['NewDeaths'].fillna(0).astype(int)
USCounties4[['Confirmed', 'Deaths',
 'Ventilators_Average',
       'POP_ESTIMATE_2018', 'POVALL_2018',  'Unemployed_2018',
        'Median_Household_Income_2018', 'Recovered', 'Active',
       'State_Confirmed', 'State_Deaths', 'State_Recovered',
        'State_Testing']]=USCounties4[['Confirmed', 'Deaths', 
        'Ventilators_Average',
       'POP_ESTIMATE_2018', 'POVALL_2018',  'Unemployed_2018',
        'Median_Household_Income_2018', 'Recovered', 'Active',
       'State_Confirmed', 'State_Deaths', 'State_Recovered',
        'State_Testing']].fillna(0).astype(int)



#Add url and Thumbnail columns
fiplist=USCounties4['FIPS'].tolist()
urllist=list()
for i in fiplist:
    url0='https://bao.arcgis.com/covid-19/jhu/county/'+i+'.html'
    urllist.append(url0)
USCounties4['url']=urllist
USCounties4['Thumbnail']="https://coronavirus.jhu.edu/static/media/dashboard_infographic_thumbnail.png"



tdtime=datetime.strftime(datetime.now(), '%m/%d/%Y %H:%M:%S')
# print (tdtime)
USCounties4['DateChecked']=tdtime
# USCounties4['DateChecked']


#reorganize the field and export
USCounties4=USCounties4[['Countyname', 'ST_Name','ST_Abbr', 'ST_ID','geometry',
       'FIPS', 'FatalityRate', 'ConfirmedbyPop','DeathsbyPop', 'PCTPOVALL_2018', 
         'Unemployment_rate_2018', 'Med_HH_Income_Percent_of_State_Total_2018',
       'State_FatalityRate', 'DateChecked',
        'EM_type', 'EM_date','EM_notes','url', 'Thumbnail', 'Confirmed',  'Deaths',
        'Age_85', 'Age_80_84', 'Age_75_79', 'Age_70_74', 'Age_65_69',  
        'Beds_Licensed', 'Beds_Staffed','Beds_ICU', 'Ventilators_Average', 
        'POP_ESTIMATE_2018','POVALL_2018', 'Unemployed_2018','Median_Household_Income_2018',
        'Recovered', 'Active', 'State_Confirmed', 'State_Deaths', 'State_Recovered',
       'State_Testing',  'AgedPop','NewCases', 'NewDeaths','TotalPop',
       'NonHispWhPop', 'BlackPop', 'AmIndop', 'AsianPop', 'PacIslPop',
       'OtherPop', 'TwoMorPop', 'HispPop', 'PCPopNWh', 'PCPopBk', 'PCPopAI',
       'PCPopAs', 'PPCPopPI', 'PCPopOr', 'PCPopTm', 'PCPopHL','racePop_total',
       'White alone', 'Black or African American alone',
       'American Indian and Alaska Native alone', 'Asian alone',
       'Native Hawaiian and Other Pacific Islander alone',
       'Some other race alone', 'Two or more races',
       'Not Hispanic or Latino origin', 'Hispanic or Latino Origin',
       'Age_under15', 'Age_15_24', 'Age_25_34', 'Age_35_64', 'Age_65_74',
       'Age_over75', 'Agetotal']]



USCounties4.rename(columns={'FatalityRate':'FatalityRa','ConfirmedbyPop':'Confirmedb','DeathsbyPop':'DeathsbyPo',
                            'PCTPOVALL_2018':'PCTPOVALL_','Unemployment_rate_2018':'Unemployme', 
                            'Med_HH_Income_Percent_of_State_Total_2018':'Med_HH_Inc',
                            'State_FatalityRate':'State_Fata', 'DateChecked':'DateChecke','Beds_Licensed':'Beds_Licen',
                            'Ventilators_Average':'Ventilator', 'POP_ESTIMATE_2018':'POP_ESTIMA',
                            'POVALL_2018':'POVALL_201', 'Unemployed_2018':'Unemployed',
                            'Median_Household_Income_2018':'Median_Hou',
                            'State_Confirmed':'State_Conf','State_Deaths':'State_Deat', 
                            'State_Recovered':'State_Reco','State_Testing':'State_Test',
                           'White alone':'Wh_Alone', 'Black or African American alone':'Bk_Alone',
                            'American Indian and Alaska Native alone':'AI_Alone', 'Asian alone':'As_Alone',
                            'Native Hawaiian and Other Pacific Islander alone':'NH_Alone','Some other race alone':'SO_Alone', 
                            'Two or more races':'Two_More','Not Hispanic or Latino origin':'Not_Hisp', 
                            'Hispanic or Latino Origin':'NonHisp',
                            'Age_under15':'Age_Less15', 'Age_over75':'Age_Over75',
                           },inplace=True)



USCounties4.to_file(covid19Export / 'USCounties_JHUmap.shp')



#USCounties4.to_file(r'C:\Work_GovEx\COVID-19\Daily Data\USCounties_JHUmap_Race_Age_NewCases.shp')



# USCounties4.to_file(r'C:\Work_GovEx\COVID-19\Daily Data\USCounties_JHUmap.shp')
# testcheck=gpd.read_file(r'C:\Work_GovEx\COVID-19\Daily Data\USCounties_JHUmap.shp')
# testcheck[ testcheck['Countyname']=='Washington'][['ST_Name','Confirmed','Countyname','NewCases']]


# # Update CSV



#data from github jhu,import the lastest data from timeseries
df_Counties_confirmed=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")
df_Counties_deaths=pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv")


# Exclude military and extra data added to the end
# df_Counties_confirmed=df_Counties_confirmed.iloc[:3253]

# df_Counties_deaths=df_Counties_deaths.iloc[:3253]



# check the latest date
# tdst=df_Counties_confirmed.columns[-1]
#  print (tdst)



#replace with NY boroughs files
dates_list=df_NY_confirmed.columns[4:]
# print (dates_list)

#df_NY_deaths=pd.read_csv(r'C:\Work_GovEx\COVID-19\Daily Data\JHU US Map_NY_KC_Duke_Nantucket Counties - Deaths.csv')
for days in dates_list:
    #print (days)
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[0,0],days]=df_NY_confirmed.loc[0][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[1,0],days]=df_NY_confirmed.loc[1][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[2,0],days]=df_NY_confirmed.loc[2][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[3,0],days]=df_NY_confirmed.loc[3][days]
    df_Counties_confirmed.loc[df_Counties_confirmed.FIPS==df_NY_confirmed.iloc[4,0],days]=df_NY_confirmed.loc[4][days]
    
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[0,0],days]=df_NY_deaths.loc[0][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[1,0],days]=df_NY_deaths.loc[1][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[2,0],days]=df_NY_deaths.loc[2][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[3,0],days]=df_NY_deaths.loc[3][days]
    df_Counties_deaths.loc[df_Counties_deaths.FIPS==df_NY_deaths.iloc[4,0],days]=df_NY_deaths.loc[4][days]



#deaths data has an extra column
df_Counties_deaths.drop(columns=['iso2'],inplace=True)


#convert table
def converttable(df):
    cols=df.columns.tolist()
    pd_list=[]
    for i in range(11,df.shape[1]):
        temp_cols=cols[:11]
        temp_cols.append(cols[i])
    # print(temp_cols)
        temp_pd=df[temp_cols].copy()
        temp_pd['dt']=cols[i]
        temp_pd.rename(columns={cols[i]:'value'},inplace=True)
        pd_list.append(temp_pd)
    df_new=pd.concat(pd_list,axis=0,ignore_index=True)
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
df_merged['FIPS']=df_merged['FIPS'].astype({'FIPS':'string'})


#merge with shpfiles for geometry info
US_Counties=gpd.read_file( covid19Data / "JHUCounties.shp")
df_merged1=pd.merge(df_merged,US_Counties,how='left',left_on='FIPS',right_on='GEOID')


#select columns and rename
df_merged1 = df_merged1[['Admin2','Province_State', 'FIPS','ST_ID','dt', 'confirmed', 'deaths','Population']]
df_merged1.rename(columns={'Admin2':'Countyname','Province_State':'ST_Name','ST_ID':'ST_ID','confirmed':'Confirmed','deaths':'Deaths'},inplace=True)
#Format FIPS
df_merged1['FIPS']=df_merged1['FIPS'].fillna(0).astype(int)
df_merged1['FIPS'] = df_merged1['FIPS'].apply(lambda x: '{0:0>5}'.format(x))
df_merged1['FIPS']=df_merged1['FIPS'].astype({'FIPS':'string'})
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


# df_merged1['ST_ID']=df_merged1['ST_ID'].fillna(0).astype(int)
# df_merged1['ST_ID']=df_merged1['ST_ID'].apply(str).str.pad(width=2, side='left', fillchar='0')
# df_merged1['FIPS']=df_merged1['FIPS'].fillna(0).astype(int)
# df_merged1['FIPS']=df_merged1['FIPS'].apply(str).str.pad(width=5, side='left', fillchar='0')


df_merged1.to_csv(covid19Export / 'df_Counties2020.csv')


#update the new files
df_NY_confirmed.to_csv( covid19Data / 'NY_Boroughs_Confirmed.csv')
df_NY_deaths.to_csv( covid19Data / 'NY_Boroughs_Deaths.csv')
