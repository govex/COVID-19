
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

- Non-US data sources at the country/region (Admin0) level: The international vaccine data includes Doses_admin, People_partially_vaccinated, People_fully_vaccinated. If the country does not report a variable, or the variable appears to be stale, we compare with Our World in Data and pick the most up-to-date data between the sources to produce composited data.
  - Austria Department of Health: https://info.gesundheitsministerium.gv.at/?re=opendata
  - Belgium Institute of Health (Sciensano): https://info.gesundheitsministerium.gv.at/?re=opendata
  - Bulgaria Unified Information Portal: https://coronavirus.bg/bg/statistika
  - Canada COVID-19 Tracker: https://covid19tracker.ca/vaccinationtracker.html
  - Government of Chile: https://www.gob.cl/yomevacuno/
  - Denmark Statum Serum Institute: https://experience.arcgis.com/experience/1c7ff08f6cef4e2784df7532d16312f1
  - Government of France: https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19-1/
  - Germany Federal Ministry of Health: https://impfdashboard.de/
  - Government of India: https://www.mohfw.gov.in/
  - Government of Ireland: https://covid19ireland-geohive.hub.arcgis.com/ 
  - Italy Ministry of Health: https://www.governo.it/it/cscovid19/report-vaccini/
  - Latvia National Health Service: https://data.gov.lv/dati/eng/dataset/covid19-vakcinacijas#
  - Luxembourg Ministry of Health: https://data.public.lu/fr/datasets/covid-19-rapports-journaliers/#_
  - Government of Poland: https://www.gov.pl/web/szczepimysie/raport-szczepien-przeciwko-covid-19
  - Spain Ministry of Health: https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov/pbiVacunacion.htm
  - United Arab Emirates Supreme Council for National Security: https://covid19.ncema.gov.ae/en
  - Government of Ukraine: https://health-security.rnbo.gov.ua/vaccination
  - United Kingdom Government: https://coronavirus.data.gov.uk/
