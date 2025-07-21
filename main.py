# This code is written in python
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell175.csv")

column = "ED_attainment_secondary_higher_p"

print("max: " + str(round(lwd[column].max())))
print("min: " + str(round(lwd[column].min())))

#Change x here:
numBins = 29
histRange = (0,100)
histX, histY, _ = plt.hist(x=column, data=lwd, edgecolor='white', bins=numBins)
binVal = np.argmax(histX)
print("common: " + str(round((histY[binVal] + (histY[binVal] + histRange[1] / numBins))/2, 2)))
print("mean: " + str(round(lwd[column].mean(), 2)))
print('median: ' + str(round(lwd[column].median(), 2)))

#Change x-label here:
plt.xlabel("Human Development Index")

plt.ylabel("Number of Data Points")
plt.show()