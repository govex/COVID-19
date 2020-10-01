# **************************** UNCLASSIFIED ****************************
# Copyright (C) 2020 Johns Hopkins University Applied Physics Laboratory
# 
# All Rights Reserved.
# This material may only be used, modified, or reproduced by or for the
# U.S. government persuant to the license rights granted under FAR
# clause 52.227-14 or DFARS clauses 252.227-7013/7014.
# For any other permission, please contact the Legal Office at JHU/APL.
# **********************************************************************

import numpy as np

def correct_and_smooth(row, smoother):
    # Correct confirmed cases data for errors
    confirmed_cases_list = row.tolist()
    confirmed_cases_deltas = np.zeros(shape=(len(confirmed_cases_list)))
    for index2, confirmed_cases in enumerate(confirmed_cases_list):

        # If c[i] = 0, c[i] = c[i-1]
        if confirmed_cases == 0 and index2 != 0:
            confirmed_cases_list[index2] = confirmed_cases_list[index2 - 1]
        
        # Get deltas
        confirmed_cases_deltas[index2] = confirmed_cases_list[index2] - confirmed_cases_list[index2 - 1]

        # If a delta is negative, set it to zero
        if confirmed_cases_deltas[index2] < 0:
            confirmed_cases_deltas[index2] = 0
    
    # Smooth confirmed cases data
    smoothed_confirmed_cases_deltas = smoother.getSmoothedValues(confirmed_cases_deltas)

    return smoothed_confirmed_cases_deltas
