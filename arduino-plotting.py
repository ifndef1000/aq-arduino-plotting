# /*********************************************/
# Arduino CSV C++ sequence of data:
# BME: Date (YYYY/MM/DD) // Time (HH:MM:SS) // Temperature (C) // Pressure (Pa) // Humidity (%) // Gas Resistance (kOhms)
# GAS: Date (YYYY/MM/DD) // Time (HH:MM:SS) // NO2 // C2H5OH or Ethanol // VOC // CO
# PM: Date (YYYY/MM/DD) // Time (HH:MM:SS) // Mass Concentration PM2.5 (micrograms per m3) // MC PM10 (micrograms per m3) // Number Concentration PM 2.5 (number per cm3) // NC PM10 (number per cm3) // Typical particle size (micrometer)
# /********************************************/

from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import os
import numpy as np
import pandas as pd


## Global definitions ##
fig, ax = plt.subplots(3,3, figsize=(10, 10), dpi=100) ## creates the general canvas



marker_size = 10 ## marker size
num_rows = 3305 ## max number of rows
trfont = {'fontname':'Times New Roman'} ## font class
afont = {'fontname':'Arial'} ## font class
delimiter_symbol = ',' ## delimeter symbol for the CSV files, in this case commas only
plt.xticks(**trfont, fontsize=12) ## all xticks to have times new romans and font size 12
plt.yticks(**trfont, fontsize=12) ## all yticks to have times new romans and font size 12

## Path for the CSV data
data_path = 'D:\\Google Drive\\003.Liverpool John Moores University\\004.Level 6 (third year)\\6226BEUG DISSERTATION\\00.Arduino\Data\\2020.12.12 Experimental Data'

## Picks up the CSV files and converts them into dataframes, skips row 0. Make sure to change the .CSV names if you've changed the arduino output filenames
bme = pd.read_csv(data_path + '\\' + 'BME.CSV', sep=delimiter_symbol, delimiter=None, nrows=num_rows, skiprows=0)
gas = pd.read_csv(data_path + '\\' + 'GAS.CSV', sep=delimiter_symbol, delimiter=None,nrows=num_rows, skiprows=0)
pm = pd.read_csv(data_path + '\\' + 'PM.CSV', sep=delimiter_symbol, delimiter=None,nrows=num_rows, skiprows=0)

### GASES ############################################################################################################################################################

###/ NO2 PLOTTING CODE BEGINS /###
y0 = gas.iloc[:, 2] ## column 3, all rows from the df
x0 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[0,0].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[0,0].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[0,0].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,0].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,0].set_axisbelow(True) ## makes sure that the plotting is below the graph
## Sets the labels, together with the font styles and sizes
ax[0,0].set_title('$NO_2$ (Grove)')
ax[0,0].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[0,0].set_ylabel('$NO_2$ (ppm)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[0,0].scatter(x0,y0, s=marker_size, marker='.', color='black')
###/ NO2 PLOTTING CODE ENDS /###

###/ Ethanol PLOTTING CODE BEGINS /###
y1 = gas.iloc[:, 3] ## column 3, all rows from the df
x1 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[1,0].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[1,0].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[1,0].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,0].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,0].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[1,0].set_title('Ethanol (Grove)')
## Sets the labels, together with the font styles and sizes
ax[1,0].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[1,0].set_ylabel('$C_{2}H_{5}OH$ (ppm)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[1,0].scatter(x1,y1, s=marker_size, marker='.', color='black')
###/ ETHANOL PLOTTING CODE ENDS /###

###/ CARBON MONOXIDE (C0) /###
y2 = gas.iloc[:, 4] ## column 3, all rows from the df
x2 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[2,0].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[2,0].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[2,0].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,0].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,0].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[2,0].set_title('CO (Grove)')
## Sets the labels, together with the font styles and sizes
ax[2,0].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[2,0].set_ylabel('CO (ppm)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[2,0].scatter(x2,y2, s=marker_size, marker='.', color='black')
###/ CARBON MONOXIDE (C0) /###

###/ GROVE VOC (ppm)) /###
y3 = gas.iloc[:, 5] ## rows, columns, two dots means all
x3 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[2,1].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[2,1].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[2,1].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,1].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,1].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[2,1].set_title('VOC (Grove)')
## Sets the labels, together with the font styles and sizes
ax[2,1].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[2,1].set_ylabel('VOC (ppm)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[2,1].scatter(x3,y3, s=marker_size, marker='.', color='black')
###/ GROVE VOC (ppm)) /###

### BME SENSOR ############################################################################################################################################################

###/ TEMPERATURE (deg C) /###
y3 = bme.iloc[:, 2] ## rows, columns, two dots means all
x3 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[0,1].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[0,1].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[0,1].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,1].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,1].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[0,1].set_title('Temperature (BME680)')
## Sets the labels, together with the font styles and sizes
ax[0,1].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[0,1].set_ylabel('Temperature (°C)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[0,1].scatter(x3,y3, s=marker_size, marker='.', color='black')
###/ TEMPERATURE (deg C) /###

###/ HUMIDITY (%) /###
y4 = bme.iloc[:, 4] ## rows, columns, two dots means all
x4 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[1,1].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[1,1].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[1,1].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,1].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,1].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[1,1].set_title('Humidity (BME680)')
## Sets the labels, together with the font styles and sizes
ax[1,1].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[1,1].set_ylabel('Humidity (%)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[1,1].scatter(x4,y4, s=marker_size, marker='.', color='black')
###/ HUMIDITY (%) /###

### PARTICULATE MATTER ############################################################################################################################################################

###/ PM (2.5 micrograms per m3) /###
y5 = pm.iloc[:, 2] ## rows, columns, two dots means all
x5 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[0,2].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[0,2].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[0,2].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,2].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[0,2].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[0,2].set_title('PM 2.5 (SPS30)')
## Sets the labels, together with the font styles and sizes
ax[0,2].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[0,2].set_ylabel('PM 2.5 ($μg/m^3$)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[0,2].scatter(x5,y5, s=marker_size, marker='.', color='black')
###/ PM (2.5 micrograms per m3) /###

###/ PM (10 micrograms per m3) /###
y6 = pm.iloc[:, 3] ## rows, columns, two dots means all
x6 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[1,2].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[1,2].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[1,2].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,2].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[1,2].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[1,2].set_title('PM 10 (SPS30)')
## Sets the labels, together with the font styles and sizes
ax[1,2].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[1,2].set_ylabel('PM 10 ($μg/m^3$)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[1,2].scatter(x6,y6, s=marker_size, marker='.', color='black')
###/ PM (10 micrograms per m3) /###

###/ Typical Particle Size (micrometers) /###
y7 = pm.iloc[:, 6] ## rows, columns, two dots means all
x7 = (range(1,num_rows)) ## range for the time variable, asuming 1 second per row/reading
ax[2,2].grid(b=True, which='major',linestyle='-', linewidth='0.5', color='#666666') ## creates the major grid, with a straight linestile and 0.5 lineweight
ax[2,2].grid(b=True, which='minor',linestyle='-', linewidth='0.5', color='#999999', alpha=0.2) ## creates the minor grid, with a straight linestile and 0.5 lineweight
ax[2,2].xaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,2].yaxis.set_minor_locator(AutoMinorLocator(4)) ## creates minor locators, 4 for every major locator
ax[2,2].set_axisbelow(True) ## makes sure that the plotting is below the graph
ax[2,2].set_title('Typical Particle Size (SPS30)')
## Sets the labels, together with the font styles and sizes
ax[2,2].set_xlabel('Time (s)', fontstyle='italic', **trfont, fontsize=12)
ax[2,2].set_ylabel('Typical Particle Size (μm)', fontstyle='italic', **trfont, fontsize=12) 
## Plots the scatter, using two variables, and defines the marker size as well as the type of marker
ax[2,2].scatter(x7,y7, s=marker_size, marker='.', color='black')
###/ Typical Particle Size (micrometers) /###



### SAVING FIGURE ############################################################################################################################################################

fig.suptitle('Indoor sensor testing for 1 hour (14:30 PM)', fontsize=30, **trfont)
plt.tight_layout()
plt.show() ## shows the plot, uncomment if you want to see
plt.savefig(data_path + '\\Plots.pdf', dpi=80) ## Saves the plot
