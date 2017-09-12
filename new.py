import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy import nan as NA
import glob

ferms = glob.glob ('/home/kilimanjaro2/CCNSB/Final/Alanine/60_length/csv files/*.csv')
#print ferms
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
paramnames = ["id","msd","msdder"]

for ferm in ferms:
    # define the dataframe
    data = pd.read_csv(ferm,names = paramnames)
    # print data[1]
    ax.plot(data['id'], data['msd'])

plt.xlabel('Timestep')
plt.ylabel('MSD (Angstroms)')
plt.show()
