# U.S. testing data


## Files in this folder
- [data_dictionary.csv](https://github.com/govex/COVID-19/blob/master/data_tables/testing_data/data_dictionary.csv): Metric definitions and column name equivalences with CTP.
- [tests_combined_total_source.csv](https://github.com/govex/COVID-19/blob/master/data_tables/testing_data/tests_combined_total_source.csv): For each state, a reference to the data field used to produce the tests_combined_total metric.

## Forthcoming Updates (11/23/20210
The JHU Coronavirus Resource Center is updating and expanding some of itstesting resources.  The previous version of the timeseries file has been moved into the archive folder under the name _legacy, and the new file is time_series_covid19_US.csv: https://github.com/govex/COVID-19/blob/master/data_tables/testing_data/time_series_covid19_US.csv. The new file has people_viral_positive information for certain states where the data is publicly available, backfilled when possible. The legacy file will be removed in 2-3 weeks to allow time for transition.

## Transition from Covid Tracking Project (CTP)
The Johns Hopkins Coronavirus Resource Center provides U.S. state testing data from publicly reported sources, a service that replaces the [COVID Tracking Project](https://covidtracking.com/)’s year-long collection effort ending March 7, 2021.

Our files will include Covid Tracking Project data up to March 3, 2021, and data collected by JHU from that date forward. The [data dictionary](https://github.com/govex/COVID-19/blob/master/data_tables/testing_data/data_dictionary.csv) details all the variables' name equivalences to match CTP to JHU names.

The CTP dataset field named 'totalTestResults' contains total viral tests in a variety of units (test specimens, encounters, or unique people). We list what unit is used for what state in the file [tests_combined_total_source.csv](https://github.com/govex/COVID-19/blob/master/data_tables/testing_data/tests_combined_total_source.csv)

Antigen data is anticipated, though not yet available.

## API
We are providing an up to date, read only version of our testing data in JSON format at this location. 
https://jhucoronavirus.azureedge.net/api/v1/testing/daily.json
This API contains only testing data at this time.

## Data sources
Our data sources are a combination of the State's public dashboards, and, when that data is not available at a frequent cadence, the U.S. Department of Health & Human Services: https://healthdata.gov/dataset/COVID-19-Diagnostic-Laboratory-Testing-PCR-Testing/j8mb-icvb

- AK: https://alaska-coronavirus-vaccine-outreach-alaska-dhss.hub.arcgis.com/app/ed1c874ca60b4c15ab09095a070065ca
- AL: https://alpublichealth.maps.arcgis.com/apps/opsdashboard/index.html#/6d2771faa9da4a2786a509d82c8cf0f7
- AR: https://experience.arcgis.com/experience/c2ef4a4fcbe5458fbf2e48a21e4fece9
- AZ: https://www.azdhs.gov/preparedness/epidemiology-disease-control/infectious-disease-epidemiology/covid-19/dashboards/index.php
- CA: https://covid19.ca.gov/state-dashboard/
- CO: https://public.tableau.com/views/Colorado_COVID19_Data/CO_Hospital?%3Aembed=y&%3AshowVizHome=no
- CT: https://data.ct.gov/coronavirus, https://data.ct.gov/Health-and-Human-Services/COVID-19-PCR-Based-Test-Results-by-Date-of-Specime/qfkt-uahj
- DC: https://coronavirus.dc.gov/data
- DE: https://myhealthycommunity.dhss.delaware.gov/locations/state/days_to_show/169/primary_trend_type/bar#trends_dashboard
- FL: http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/cases-monitoring-and-pui-information/state-report/state_reports_latest.pdf, http://ww11.doh.state.fl.us/comm/_partners/covid19_report_archive/total-antibody-results/serology-reports/serology_latest.pdf
- GA: https://dph.georgia.gov/covid-19-daily-status-report
- GU: http://dphss.guam.gov/covid-19/, https://drive.google.com/file/d/1FVW6sNbdgyV5-CYkOorYvOGivkmOED8t/view
- HI: https://health.hawaii.gov/coronavirusdisease2019/what-you-should-know/current-situation-in-hawaii/, https://hiema.maps.arcgis.com/apps/opsdashboard/index.html#/9a19e1adeceb46c58185cb0396faf36b
- IA: https://coronavirus.iowa.gov/
- ID: https://public.tableau.com/profile/idaho.division.of.public.health#!/vizhome/DPHIdahoCOVID-19Dashboard/Home
- IL: http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus
- IN: https://www.coronavirus.in.gov/2393.htm
- KS: https://www.coronavirus.kdheks.gov/160/COVID-19-in-Kansas
- KY: https://govstatus.egov.com/kycovid19, https://chfs.ky.gov/agencies/dph/covid19/COVID19DailyReport.pdf
- LA: https://ldh.la.gov/Coronavirus/
- MA: https://www.mass.gov/info-details/covid-19-response-reporting#covid-19-daily-dashboard-
- MD: https://coronavirus.maryland.gov/
- ME: https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus/data.shtml
- MI: https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html
- MN: https://www.health.state.mn.us/diseases/coronavirus/situation.html#casesm1
- MO: https://showmestrong.mo.gov/data/public-health/testing/
- MP: https://cnmichcc.maps.arcgis.com/apps/opsdashboard/index.html#/4061b674fc964efe84f7774b7979d2b5
- MS: https://msdh.ms.gov/msdhsite/_static/14,0,420.html
- MT: https://montana.maps.arcgis.com/apps/MapSeries/index.html?appid=7c34f3412536439491adcc2103421d4b, https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt/demographics
- NC: https://covid19.ncdhhs.gov/dashboard/testing
- ND: https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases
- NE: https://experience.arcgis.com/experience/ece0db09da4d4ca68252c3967aa1e9dd/page/page_0/
- NH: https://www.nh.gov/covid19/dashboard/map.htm#dash, https://www.nh.gov/covid19/
- NJ: https://covid19.nj.gov/
- NM: https://cv.nmhealth.org/
- NV: https://nvhealthresponse.nv.gov/
- NY: https://covid19tracker.health.ny.gov/views/NYS-COVID19-Tracker/NYSDOHCOVID-19Tracker-TableView?%3Aembed=yes&%3Atoolbar=no&%3Atabs=n
- OH: https://data.ohio.gov/wps/portal/gov/data/view/covid-nineteen-key-metrics-on-testing
- OK: https://oklahoma.gov/covid19.html, https://oklahoma.gov/covid19/newsroom/executive-order-reports.html
- OR: https://govstatus.egov.com/OR-OHA-COVID-19
- PA: https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx
- PR: https://bioseguridad.maps.arcgis.com/apps/opsdashboard/index.html#/3bfb64c9a91944bc8c41edd8ff27e6df
- RI: https://docs.google.com/spreadsheets/d/1c2QrNMz8pIbYEKzMJL7Uh2dtThOJa2j1sSMwiDo5Gz4/edit#gid=264100583, https://ri-department-of-health-covid-19-data-rihealth.hub.arcgis.com/
- SC: https://scdhec.gov/infectious-diseases/viruses/coronavirus-disease-2019-covid-19/sc-testing-data-projections-covid-19
- SD: https://doh.sd.gov/COVID/Dashboard.aspx
- TN: https://www.tn.gov/content/tn/health/cedep/ncov/data.html, https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/datasets/Public-Dataset-Daily-Case-Info.XLSX
- TX: https://txdshs.maps.arcgis.com/apps/opsdashboard/index.html#/0d8bdf9be927459d9cb11b9eaef6101f
- UT: https://coronavirus-dashboard.utah.gov/
- VA: https://www.vdh.virginia.gov/coronavirus/covid-19-in-virginia/
- VI: https://doh.vi.gov/covid19usvi
- VT: https://experience.arcgis.com/experience/85f43bd849e743cb957993a545d17170
- WA: https://www.doh.wa.gov/Emergencies/COVID19/DataDashboard, https://www.doh.wa.gov/Portals/1/Documents/1600/coronavirus/data-tables/PUBLIC_Tests_by_Specimen_Collection.xlsx
- WI: https://www.dhs.wisconsin.gov/covid-19/data.htm
- WV: https://dhhr.wv.gov/COVID-19/Pages/default.aspx
- WY: https://health.wyo.gov/publichealth/infectious-disease-epidemiology-unit/disease/novel-coronavirus/covid-19-testing-data/

