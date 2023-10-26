# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 02:13:41 2023

@author: StudentIn
"""

import pandas as pd  # useful for processing csv files
import matplotlib.pyplot as plt  # useful for plotting
import numpy as np

# import csv file with pandas
data = pd.read_csv("ClimateData.csv", sep=";", index_col="Decade")

# plot the time series

##############
#YOUR CODE HERE
##############
fig, axes = plt.subplots(3, figsize=(6, 12))

data.plot(y="GlobalAvgTemp", ax=axes[0], color="red", marker="o") # plot the global average temperature on the first subplot
data.plot(y="NmbrPirates", ax=axes[1], color="blue", marker="o") # plot the number of pirates on the second subplot
data.plot(y="Co2Concentration",ax=axes[2], color="green", marker="o") # plot the CO2 concentration on the third subplot
for ax in fig.axes:
    ax.grid()
plt.tight_layout() # adjust the spacing between subplots
plt.show()

##############

# calculate correlation coefficient
# you may use any library functions for this! 
# (you don't have to write the calculation yourself)

##############
#YOUR CODE HERE
##############

# use the corr method to calculate the Pearson correlation coefficient
r1 = data["GlobalAvgTemp"].corr(data["NmbrPirates"]) # correlation between GlobalAvgTemp and NmbrPirates
r2 = data["GlobalAvgTemp"].corr(data["Co2Concentration"]) # correlation between GlobalAvgTemp and Co2Concentration
# print the results
print("Correlation coefficients\n")
print("global avg. temperature - number of pirates:", r1)
print("global avg. temperature - average Co2 Concentration:", r2)

##############

# Vizualitation of the correlation

##############
#YOUR CODE HERE
##############

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# plot the scatter plot and the regression line for r1
data.plot.scatter(x="GlobalAvgTemp", y="NmbrPirates", ax=axes[0], color="blue")

axes[0].plot(np.unique(data["GlobalAvgTemp"]), np.poly1d(np.polyfit(data["GlobalAvgTemp"], data["NmbrPirates"], 1))(np.unique(data["GlobalAvgTemp"])), color="red")
axes[0].set_title(f"Correlation coefficient: {r1:.3f}")

# plot the scatter plot and the regression line for r2
data.plot.scatter(x="GlobalAvgTemp", y="Co2Concentration", ax=axes[1], color="green")

axes[1].plot(np.unique(data["GlobalAvgTemp"]), np.poly1d(np.polyfit(data["GlobalAvgTemp"], data["Co2Concentration"], 1))(np.unique(data["GlobalAvgTemp"])), color="red")
axes[1].set_title(f"Correlation coefficient: {r2:.3f}")

plt.tight_layout() 
plt.show()

##############