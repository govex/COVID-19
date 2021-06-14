
# International vaccine data

## Files in this folder

- time_series_covid19_vaccine_global.csv: Contains time series data. Each row is uniquely defined by `country` and `date`. Long format.
- time_series_covid19_vaccine_doses_admin_global.csv: Contains time series data. Each row is uniquely defined by `country` and `date`Wide format.
- vaccine_data_global.csv: Contains the most recent data collected for each country. Each row is uniquely defined by `country`
- data_dictionary.csv: Metric definitions
- readme.md: Description of contents and list of data sources

## Data sources

- Aggregated data sources:
  - US Centers for Disease Control and Prevention (CDC): https://covid.cdc.gov/covid-data-tracker/#vaccinations
  - Our World in Data (OWiD): https://ourworldindata.org/covid-vaccinations
  - World Health Organization (WHO): https://covid19.who.int/who-data/vaccination-data.csv

- Non-US data sources at the country/region (Admin0) level: The international vaccine data includes Doses_admin, People_partially_vaccinated, People_fully_vaccinated. If the country does not report a variable, or the variable appears to be stale, we compare with Our World in Data and pick the most up-to-date data between the sources to produce composited data.
  - Argentina: Ministry of Health: http://datos.salud.gob.ar/dataset/vacunas-contra-covid-19-dosis-aplicadas-en-la-republica-argentina/archivo/b4684dd9-3cb7-45f7-9c0e-086550013e22
  - Austria: Department of Health: https://info.gesundheitsministerium.gv.at/?re=opendata
  - Bangladesh: Directorate General of Health Services: http://103.247.238.92/webportal/pages/covid19-vaccination-update.php
  - Belgium: Institute of Health (Sciensano): https://covid-vaccinatie.be/en
  - Brazil: Ministry of Health: https://qsprod.saude.gov.br/extensions/DEMAS_C19Vacina/DEMAS_C19Vacina.html
  - Bulgaria: Unified Information Portal: https://coronavirus.bg/bg/statistika
  - Canada: COVID-19 Tracker: https://covid19tracker.ca/vaccinationtracker.html
  - Chile: Government of Chile: https://www.gob.cl/yomevacuno/
  - Colombia: Ministry of Health and Social Protection: https://www.minsalud.gov.co/portada-covid-19.html
  - Denmark: Statum Serum Institute: https://experience.arcgis.com/experience/1c7ff08f6cef4e2784df7532d16312f1
  - France: Government of France: https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/
  - Germany: Federal Ministry of Health: https://impfdashboard.de/
  - Guatemala: Ministry of Public Health and Social Assistance: https://tablerocovid.mspas.gob.gt/
  - Hong Kong: Government of Hong Kong Special Administration Region: https://www.covidvaccine.gov.hk/en/dashboard
  - India: Government of India: https://www.mygov.in/covid-19
  - Israel: Israel Ministry of Health: https://datadashboard.health.gov.il/COVID-19/general
  - Ireland: Government of Ireland: https://covid19ireland-geohive.hub.arcgis.com/ 
  - Italy: Ministry of Health: https://www.governo.it/it/cscovid19/report-vaccini/
  - Japan: Prime Minister of Japan and His Cabinet: https://www.kantei.go.jp/jp/headline/kansensho/vaccine.html 
  - Latvia: National Health Service: https://data.gov.lv/dati/eng/dataset/covid19-vakcinacijas#
  - Luxembourg: Ministry of Health: https://data.public.lu/fr/datasets/covid-19-rapports-journaliers/#_
  - New Zealand: Ministry of Health: https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-vaccine-data
  - Netherlands, The: Central Government of the Netherlands: https://coronadashboard.rijksoverheid.nl/landelijk/vaccinaties
  - Norway: Public Health Institute: https://www.fhi.no/sv/vaksine/koronavaksinasjonsprogrammet/koronavaksinasjonsstatistikk/#table-pagination-66720844
  - Pakistan: Government of Pakistan: https://ncoc.gov.pk/covid-vaccination-en.php
  - Paraguay: Ministry of Health and Social Wellness: https://www.vacunate.gov.py/index-listado-vacunados.html
  - Peru: Ministry of Health: https://gis.minsa.gob.pe/GisVisorVacunados/
  - Poland: Government of Poland: https://www.gov.pl/web/szczepimysie/raport-szczepien-przeciwko-covid-19
  - Portugal: General Health Management: https://esriportugal.maps.arcgis.com/apps/opsdashboard/index.html#/acf023da9a0b4f9dbb2332c13f635829
  - Russia: Gogov: https://gogov.ru/articles/covid-v-stats 
  - Saudi Arabia: Ministry of Health: https://covid19.moh.gov.sa/
  - Singapore: Ministry of Health: https://www.moh.gov.sg/covid-19
  - South Africa: Republic of South Africa Department of Health: https://sacoronavirus.co.za/
  - Spain: Ministry of Health: https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov/pbiVacunacion.htm
  - Sri Lanka: Ministry of Health Epidemiology Unit: http://www.epid.gov.lk/web/index.php?option=com_content&view=article&id=225&lang=en
  - Suriname: Ministry of Health: https://laatjevaccineren.sr/
  - Turkey: Ministry of Health: https://covid19asi.saglik.gov.tr/
  - United Arab Emirates: Supreme Council for National Security: https://covid19.ncema.gov.ae/en
  - Ukraine: Government of Ukraine: https://health-security.rnbo.gov.ua/vaccination
  - United Kingdom: United Kingdom Government: https://coronavirus.data.gov.uk/
  - Uruguay: Ministry of Public Health: https://monitor.uruguaysevacuna.gub.uy/
