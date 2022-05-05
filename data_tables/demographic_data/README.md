# COVID-19 Demographic Data
The Johns Hopkins Coronavirus Resource Center (CRC) started collecting demographic data of COVID-19 cases, deaths, people tested, and people vaccinated from various state sources. The CRC updates this repository every two weeks for tests and vaccines and every month for cases and deaths. The CRC currently collects data on age, gender or sex, race only (not including Hispanic or Latino ethnicity), ethnicity only, and race and ethnicity combined depending on the availability from the state or territory. The availability of data for state/territory-specific demographic groups or estimates depends entirely on the state or territorial source, and it might change across time.   

[Demographics_by_state_raw.csv](demographics_by_state_raw.csv) contains data using state/territory-specific naming for each demographic group and different types of estimates. On the other hand, [Demographics_by_state_standardized.csv](demographics_by_state_standardized.csv) undergoes a data cleaning process (detailed [here](COVID19_demographics_standardization_process.md)) that produces a dataset with standard demographic groups across all states and territories.

## Files in this folder
- [Demographics_by_state_raw.csv](demographics_by_state_raw.csv). Contains demographic data for COVID-19 cases, deaths, testing, and vaccination starting from 4/2/2021. Data is presented as collected from each state dasbhoard without any data processing. Each row is uniquely defined by `Category`, `Metric`, `Demo_cat_0`, `Demo_cat_1`, and `Estimate_type`. Data on Cases and Deaths will be updated on a monthly basis while Testing and Vaccination data every 14 days.
- [COVID19_demographics_data_dictionary.md](COVID19_demographics_data_dictionary.md). Contains the definition of all variables contained in the Demographics_by_state_raw.csv file.
- [Demographics_by_state_standardized.csv](demographics_by_state_standardized.csv). Contains standardized demographic data for COVID-19 cases, deaths, testing, and vaccination starting from 4/2/2021. Data from each state dashboard was processed to produce a dataset with standard demographic categories and estimates across states with available data. Each row is uniquely defined by `Category`, `Metric`, `Demo_cat_0`, `Demo_cat_1`, and `Estimate_type`. Data on cases and deaths will be updated on a monthly basis while testing and vaccination data every 14 days.
- [COVID19_demographics_standardized_data_dictionary.md](COVID19_demographics_standardized_data_dictionary.md) Contains the definition of all variables contained in the Demographics_by_state_standardized.csv file.
- [COVID19_demographics_standardization_process.md](COVID19_demographics_standardization_process.md). Contains the description of the process followed to transform the raw data from Demographics_by_state_raw.csv into a standardized dataset with similar demographic categories and groups across all states where data was available. The output is located in Demographics_by_state_standardized.csv

## Data sources by state
### AL
- Cases and deaths: https://covid19.alabama.gov/
- Vaccines: https://www.alabamapublichealth.gov/covid19vaccine/data.html
### AK
- Cases, deaths, and vaccines: https://alaska-coronavirus-vaccine-outreach-alaska-dhss.hub.arcgis.com/
### AR
- Cases, deaths, and vaccines: https://experience.arcgis.com/experience/c2ef4a4fcbe5458fbf2e48a21e4fece9 
### AZ
- Cases, deaths, tests, and vaccines: https://www.azdhs.gov/preparedness/epidemiology-disease-control/infectious-disease-epidemiology/covid-19/dashboards/index.php
### CA
- Cases and deaths: https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state/resource/4d93df07-7c4d-4583-af53-03f950fe4365
- Tests: https://covid19.ca.gov/equity/
- Vaccines: https://covid19.ca.gov/vaccines/#California-vaccines-dashboard
### CO
- Cases and deaths: https://drive.google.com/drive/folders/17MWRnHYUhlv19CnoFxbRj3OTGBqlPaar
- Vaccines: https://drive.google.com/drive/folders/1r095ofG8YvNj_dMWEq4XKkfhDaF8-I0n
### CT
- Cases and deaths: https://data.ct.gov/stories/s/q5as-kyim
- Vaccines: https://data.ct.gov/stories/s/CoVP-COVID-Vaccine-Distribution-Data/bhcd-4mnv/
### DC
- Cases and deaths: https://coronavirus.dc.gov/data
- Vaccines: https://coronavirus.dc.gov/data/vaccination
### FL
- Cases and deaths: http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/cases-monitoring-and-pui-information/state-report/state_reports_latest.pdf
- Vaccines: http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/vaccine/vaccine_report_latest.pdf
- Weekly report for Cases, Deaths, and Vaccines after 7/2/2021: http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/covid19-data/covid19_data_latest.pdf
### GA
- Cases and deaths: https://dph.georgia.gov/covid-19-daily-status-report
- Vaccines: https://experience.arcgis.com/experience/3d8eea39f5c1443db1743a4cb8948a9c 
### GU
- Cases and deaths: http://dphss.guam.gov/covid-19/
### HI
- Cases, deaths, and vaccines before 3/11/2022: https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/
- Cases by age and gender or sex: https://health.hawaii.gov/coronavirusdisease2019/tableau_dashboard/outcome-data/
- Cases by race and ethnicity: https://health.hawaii.gov/coronavirusdisease2019/tableau_dashboard/race-ethnicity-data/
- Deaths: https://health.hawaii.gov/coronavirusdisease2019/tableau_dashboard/mortality-data/
- Vaccines: https://health.hawaii.gov/coronavirusdisease2019/tableau_dashboard/21778/
### IA
- Cases: https://coronavirus.iowa.gov/pages/case-counts 
- Deaths: https://coronavirus.iowa.gov/pages/outcome-analysis-deaths
- Vaccines: https://coronavirus.iowa.gov/pages/vaccineinformation#VaccineInformation
- Cases, Deaths, and Vaccines after 2/15/2022: https://idph.iowa.gov/Emerging-Health-Issues/Novel-Coronavirus/COVID-19-Reporting?utm_medium=email&utm_source=govdelivery
### IN
- Cases, deaths, and tests: https://hub.mph.in.gov/dataset/covid-19-case-demographics
- Vaccines: https://hub.mph.in.gov/dataset/covid-19-vaccinations-demographics-by-county-and-district
### ID
- Cases and deaths: https://public.tableau.com/profile/idaho.division.of.public.health#!/vizhome/DPHIdahoCOVID-19Dashboard/Home
- Vaccines: https://public.tableau.com/profile/idaho.division.of.public.health#!/vizhome/COVID-19VaccineDataDashboard/LandingPage
### IL
- Cases, deaths, and tests: http://www.dph.illinois.gov/content/covid-19-county-historical-demographics
- Vaccines: http://www.dph.illinois.gov/covid19/vaccinedata?county=Illinois
- Vaccines after 12/3/2021: https://dph.illinois.gov/covid19/vaccine/vaccine-data.html?county=Illinois
### KS
- Cases, deaths, and tests: https://www.coronavirus.kdheks.gov/160/COVID-19-in-Kansas
- Vaccines: https://www.kansasvaccine.gov/158/Data
### KY
- Cases and deaths: https://chfs.ky.gov/agencies/dph/covid19/COVID19DailyReport.pdf
- Vaccines: https://chfs.ky.gov/agencies/dph/covid19/StatewideVaccineDemographics.pdf
- Vaccines after 4/8/2022: https://dashboard.chfs.ky.gov/views/KYPublicFacingDashboard_16191000580170/KentuckyCOVID-19Vaccination?%3Aiid=1&%3AisGuestRedirectFromVizportal=y&%3Aembed=y
### LA
- Cases and deaths: https://ladhh.maps.arcgis.com/apps/webappviewer/index.html?id=3b9b6f22d92f4d688f1c21e9d154cae2 
- Vaccines: https://ldh.la.gov/Coronavirus/
### MA
- Cases and deaths: https://www.mass.gov/info-details/covid-19-response-reporting
- Vaccines: https://www.mass.gov/info-details/massachusetts-covid-19-vaccination-data-and-updates
### MD
- Cases, deaths, and vaccines: https://coronavirus.maryland.gov/
### ME
- Cases and deaths: https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus/data.shtml
- Vaccines: https://www.maine.gov/covid19/vaccines/dashboard
### MI
- Cases and deaths (before 5/6/22): https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html
- Vaccines (before 5/6/22): https://www.michigan.gov/coronavirus/0,9753,7-406-98178_103214_103272-547150--,00.html
- Cases and deaths: https://www.michigan.gov/coronavirus/stats
- Vaccines: https://www.michigan.gov/coronavirus/resources/covid-19-vaccine/covid-19-dashboard  
### MN
- Cases: https://www.health.state.mn.us/diseases/coronavirus/situation.html#agem1
- Deaths: https://www.health.state.mn.us/diseases/coronavirus/stats/index.html#warchive1
- Vaccines:  https://mn.gov/covid19/vaccine/data/index.jsp
### MO
- Cases, deaths, and tests: https://showmestrong.mo.gov/data-download/
- Vaccines: https://showmestrong.mo.gov/data-download/vaccine/
### MP
- Cases and deaths (before 5/6/2022): https://cnmichcc.maps.arcgis.com/apps/opsdashboard/index.html#/4061b674fc964efe84f7774b7979d2b5
- Cases and deaths: https://chcc.datadriven.health/ui/99/dashboard/cbaeede2-4f75-11eb-b380-0242ac1d004a
- Vaccines: https://www.vaccinatecnmi.com/vax-dashboard/age-distribution/
### MS
- Cases and deaths: https://msdh.ms.gov/msdhsite/_static/14,0,420.html#map
- Vaccines: https://msdh.ms.gov/msdhsite/_static/14,0,420,976.html
### MT
- Cases and deaths: https://montana.maps.arcgis.com/apps/MapSeries/index.html?appid=7c34f3412536439491adcc2103421d4b
### NC
- Cases and deaths: https://covid19.ncdhhs.gov/dashboard/cases-demographics
- Vaccines: https://covid19.ncdhhs.gov/dashboard/vaccinations
### ND
- Cases: https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases
- Vaccines: https://www.health.nd.gov/covid19vaccine/dashboard
### NE
- Cases, deaths, and vaccines: https://experience.arcgis.com/experience/ece0db09da4d4ca68252c3967aa1e9dd
- Cases, deaths, and vaccines (after 9/24): https://datanexus-dhhs.ne.gov/views/Covid/1_AgeGender?%3AisGuestRedirectFromVizportal=y&%3Aembed=y&%3AdeepLinkingDisabled=y
- Cases, deaths, and vaccines (after 9/24): https://datanexus-dhhs.ne.gov/views/Covid/1_RaceEthnicity?%3AisGuestRedirectFromVizportal=y&%3Aembed=y&%3AdeepLinkingDisabled=y	
### NH
- Cases and deaths: https://www.nh.gov/covid19/dashboard/equity.htm#dash
- Testing: https://www.nh.gov/covid19/dashboard/testing.htm#dash
- Vaccines: https://www.covid19.nh.gov/dashboard/vaccination
### NJ
- Cases, deaths, and vaccines: https://covid19.nj.gov/#live-updates
### NM
- Cases: https://cvprovider.nmhealth.org/public-dashboard.html  
- Deaths: https://cv.nmhealth.org/epidemiology-reports/
- Vaccines: https://cvvaccine.nmhealth.org/public-dashboard.html
### NV
- Cases, deaths, tests, and vaccines: https://app.powerbigov.us/view?r=eyJrIjoiMjA2ZThiOWUtM2FlNS00MGY5LWFmYjUtNmQwNTQ3Nzg5N2I2IiwidCI6ImU0YTM0MGU2LWI4OWUtNGU2OC04ZWFhLTE1NDRkMjcwMzk4MCJ9
### NY
- Cases: https://covid19tracker.health.ny.gov/views/NYS-COVID19-Tracker/NYSDOHCOVID-19Tracker-DailyTracker?%3Aembed=yes&%3Atoolbar=no&%3Atabs=n
- Deaths: https://covid19tracker.health.ny.gov/views/NYS-COVID19-Tracker/NYSDOHCOVID-19Tracker-Fatalities?%3Aembed=yes&%3Atoolbar=no&%3Atabs=n
- Vaccines: https://covid19vaccine.health.ny.gov/vaccine-demographic-data
### OH
- Cases and deaths: https://coronavirus.ohio.gov/wps/portal/gov/covid-19/dashboards/demographics/case-demographics
- Vaccines: https://coronavirus.ohio.gov/wps/portal/gov/covid-19/dashboards/covid-19-vaccine/covid-19-vaccination-dashboard
### OK
- Cases: https://oklahoma.gov/covid19.html 
- Deaths: https://looker-dashboards.oklahoma.gov/embed/dashboards/76
- Vaccines: https://oklahoma.gov/covid19/newsroom/weekly-epidemiology-and-surveillance-report.html		
### OR
- Cases and deaths: https://public.tableau.com/profile/oregon.health.authority.covid.19#!/vizhome/OregonCOVID-19CaseDemographicsandDiseaseSeverityStatewide/DemographicData?:display_count=y&:toolbar=n&:origin=viz_share_link&:showShareOptions=false
- Vaccines: https://public.tableau.com/profile/oregon.health.authority.covid.19#!/vizhome/OregonCOVID-19VaccinationTrends/OregonStatewideVaccinationTrends
### PA
- Cases and deaths: https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx
- Vaccines: https://data.pa.gov/Health/Coronavirus-COVID-19-Department-of-Health-Website/98pd-gs2r 
### PR
- Cases, deaths, and vaccines: https://covid19datos.salud.gov.pr/
### RI
- Cases, deaths, and vaccines: https://docs.google.com/spreadsheets/d/1c2QrNMz8pIbYEKzMJL7Uh2dtThOJa2j1sSMwiDo5Gz4/edit#gid=31350783
### SC
- Cases and deaths: https://scdhec.gov/covid19/south-carolina-county-level-data-covid-19
- Vaccines: https://scdhec.gov/covid19/covid-19-vaccination-dashboard
### SD
- Cases, deaths, and vaccines: https://doh.sd.gov/COVID/Dashboard.aspx
### TN
- Cases, deaths and vaccines: https://www.tn.gov/health/cedep/ncov/data/downloadable-datasets.html
### TX
- Cases and deaths: https://dshs.texas.gov/coronavirus/AdditionalData.aspx
- Vaccines: https://tabexternal.dshs.texas.gov/t/THD/views/COVID-19VaccineinTexasDashboard/PeopleVaccinated?%3Aorigin=card_share_link&%3Aembed=y&%3AisGuestRedirectFromVizportal=y
### UT
- Cases, deaths, tests, and vaccines: https://coronavirus.utah.gov/case-counts/
### VA
- Cases and deaths: https://www.vdh.virginia.gov/coronavirus/coronavirus/covid-19-in-virginia-demographics/
- Vaccines: https://www.vdh.virginia.gov/coronavirus/covid-19-vaccine-demographics/
### VI
- Cases and tests: https://www.covid19usvi.com/?utm_source=doh&utm_medium=web&utm_campaign=covid19usvi
### VT 
- Cases and deaths: https://experience.arcgis.com/experience/85f43bd849e743cb957993a545d17170
- Vaccines: https://www.healthvermont.gov/covid-19/vaccine/covid-19-vaccine-dashboard
### WA
- Cases, deaths, and vaccines: https://www.doh.wa.gov/Emergencies/COVID19/DataDashboard
### WI
- Cases and deaths: https://www.dhs.wisconsin.gov/covid-19/cases.htm
- Vaccines: https://www.dhs.wisconsin.gov/covid-19/vaccine-data.htm
### WV
- Cases, deaths, and vaccines: https://dhhr.wv.gov/COVID-19/Pages/default.aspx
### WY
- Cases and deaths: https://health.wyo.gov/publichealth/infectious-disease-epidemiology-unit/disease/novel-coronavirus/covid-19-map-and-statistics/
- Tests: https://health.wyo.gov/publichealth/infectious-disease-epidemiology-unit/disease/novel-coronavirus/covid-19-testing-data/
