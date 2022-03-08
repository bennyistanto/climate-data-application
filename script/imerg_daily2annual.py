# -*- coding: utf-8 -*-
"""
NAME
    imerg_daily2annual.py
    Global IMERG annual rainfall
DESCRIPTION
    Input data for this script will use IMERG in GeoTIFF format
    This script can do annual cell statistics to get SUM or other stat: MEAN, MAX, MIN and STDEV
REQUIREMENT
    ArcGIS must installed before using this script, as it required arcpy module.
EXAMPLES
    C:\\Program Files\\ArcGIS\\Pro\\bin\\Python\\envs\\arcgispro-py3\\python imerg_daily2annual.py
NOTES
    This script is designed to work with global IMERG data
    If using other data, some adjustment are required: parsing filename, directory, threshold
CONTACT
    Benny Istanto
    Climate Geographer
    GOST, The World Bank
LICENSE
    This script is in the public domain, free from copyrights or restrictions.
VERSION
    $Id$
TODO
    xx
"""
import os
import arcpy

# Calendar year
year = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', 
        '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# Change the data and output folder
input_folder = "X:\\Temp\\imerg\\products\\wetdays\\wetdays_5mm"
output_folder = "X:\\Temp\\imerg\\products\\wetdays\\wetdays_annual_sum_5mm_temp"

dictionary = {}

for i in year:
    content = []

    for file_annual in os.listdir(input_folder):
        
        if file_annual.endswith(".tif") or file_annual.endswith(".tiff"):
            # Parsing the filename to get YYYY information
            i_imerg = file_annual.index('imerg_')
            # 6 is length of 'imerg_', and 4 is length of yyyy
            yyyy = file_annual[i_imerg + 6:i_imerg+6+4]

            if yyyy == i:
                content.append(os.path.join(input_folder, file_annual))
    
    dictionary[i] = content

for index in dictionary:
    listoffile = dictionary[index]
    print(listoffile)

    ext = ".tif"

    # Output filename
    newfilename_annual_stat1 = 'wld_cli_wetdays_5mm_annual_sum_imerg_{0}{1}'.format(index, ext)
    print(newfilename_annual_stat1)

    # Statistics type.
        # MEAN — The mean (average) of the inputs will be calculated.
        # MAJORITY — The majority (value that occurs most often) of the inputs will be determined.
        # MAXIMUM — The maximum (largest value) of the inputs will be determined.
        # MEDIAN — The median of the inputs will be calculated. Note: The input must in integers
        # MINIMUM — The minimum (smallest value) of the inputs will be determined.
        # MINORITY — The minority (value that occurs least often) of the inputs will be determined.
        # RANGE — The range (difference between largest and smallest value) of the inputs will be calculated.
        # STD — The standard deviation of the inputs will be calculated.
        # SUM — The sum (total of all values) of the inputs will be calculated.
        # VARIETY — The variety (number of unique values) of the inputs will be calculated.

    # To get another stats, you can duplicate 7 lines below and adjust the statistics type.
    # Don't forget to add additional output file name, you can copy from line 63.
    if arcpy.Exists(os.path.join(output_folder, newfilename_annual_stat1)):
        print(newfilename_annual_stat1 + " exists")
    else:
        arcpy.CheckOutExtension("spatial")
        outCellStatistics_stat1 = arcpy.sa.CellStatistics(listoffile, "SUM", "DATA")
        outCellStatistics_stat1.save(os.path.join(output_folder, newfilename_annual_stat1))
        arcpy.CheckInExtension("spatial")