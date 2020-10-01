# **************************** UNCLASSIFIED ****************************
# Copyright (C) 2020 Johns Hopkins University Applied Physics Laboratory
# 
# All Rights Reserved.
# This material may only be used, modified, or reproduced by or for the
# U.S. government persuant to the license rights granted under FAR
# clause 52.227-14 or DFARS clauses 252.227-7013/7014.
# For any other permission, please contact the Legal Office at JHU/APL.
# **********************************************************************

# --- CONFIGURATION OPTIONS ---

# Set URLs for US and Global confirmed case data
# Do not change these unless URL changes
CONFIRMED_CASES_US_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
CONFIRMED_CASES_GLOBAL_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Designate confirmed cases source
# Options are 'US' and 'global'
CONFIRMED_CASES_SOURCE = 'US'

# Aggregation is available for Province_State and Country_Region columns
AGGREGATE_BY_PROVINCE_STATE = False
AGGREGATE_BY_COUNTRY_REGION = False

# Choose whether to include testing data. Only available at the US state level
INCLUDE_STATE_TESTING_DATA = False
TESTING_URL = 'https://api.covidtracking.com/v1/states/daily.csv'

# Smoothing sensitivity. Higher = more smooth
HAMMING_SMOOTHER_WIDTH = 7

# Number of days in the past to include in the calculation
# A value of 0 will include all past data
HORIZON = 30

# Output file will be in CSV format
OUTPUT_FILENAME = 'mitigation_scores.csv'