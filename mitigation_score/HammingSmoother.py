# **************************** UNCLASSIFIED ****************************
# Copyright (C) 2020 Johns Hopkins University Applied Physics Laboratory
# 
# All Rights Reserved.
# This material may only be used, modified, or reproduced by or for the
# U.S. government persuant to the license rights granted under FAR
# clause 52.227-14 or DFARS clauses 252.227-7013/7014.
# For any other permission, please contact the Legal Office at JHU/APL.
# **********************************************************************

import math
import numpy as np

class HammingSmoother:
    def __init__(self, width):
        try:
            if width >= 0:
                self.width = width
                self.weights = self.createWeights(self.width)
        except:
            raise ValueError("Width must be an int >= 0")

    def createWeights(self, width):
        weights = np.zeros(width + 1)
        normalizer = 0.0

        for i in range(width + 1):
            value = 0.54 + 0.46 * math.cos( i * math.pi / width )
            weights[i] = value
            normalizer = normalizer + value
            if i > 0:
                normalizer = normalizer + value

        for i in range(width + 1):
            weights[i] = weights[i] / normalizer

        return weights
    
    # Accepts an array of values as input
    def getSmoothedValues(self, input):
        result = np.zeros(shape=len(input))

        for dateIndex in range(len(input)):
            summed = 0.0
            weightSum = 0.0

            for delta in range(-self.width, self.width + 1):
                inputIndex = dateIndex + delta
                if (inputIndex >= 0) and (inputIndex < len(input)):

                    weight = 0
                    if ( delta < 0 ):
                        weight = self.weights[-delta]
                    else:
                        weight = self.weights[delta]

                    summed = summed + weight * input[inputIndex]
                    weightSum = weightSum + weight
                        
            if weightSum > 0.0:
                result[dateIndex] = result[dateIndex] + summed / weightSum

        return result



