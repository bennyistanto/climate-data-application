# -*- coding: utf-8 -*-
"""
NAME
    extract_spei_dry_month.py
    
DESCRIPTION
    Input data for this script wil use TERRACLIMATE's SPEI-12, generated using pypi climate-indices
    This script will calculate number of: 
        (i)   Dry month, 
        (ii)  Total dry month
        (iii) Consecutive dry month and
        (iv)  Maximum consecutive dry month

PROCESS
    (i)   Extract TerraClimate's monthly SPEI-12 with value less than -1.2 (threshold for Moderately Dry), 1958-2020
    (ii)  If SPEI < -1.2 = Yes, then assign 1 otherwise 0. 
    (iii) For number of consecutive information, it will accumulate to next data calculation result if the value = 1. 
    	    If not, start from 0 again.
    (iv)  Total dry month derived from each dry month data
    (v)   Number of maximum conceutive months derived from each consecutive dry month data

APPLICATION
    The accumulation value will use to identified the monthly drought duration accumulation, 
    month by month, year by year.

REQUIREMENT
    ArcGIS must installed before using this script, as it required arcpy module.

NOTES
    This script is designed to work with global SPEI data generated from TerraClimate, following this guideline
    https://github.com/bennyistanto/climate-data-application/blob/main/SPEI_using_TerraClimate_data.md
    If using other data, some adjustment are required: parsing filename, directory, threshold

CONTACT
    Benny Istanto
    Climate Geographer
    GOST, The World Bank

LICENSE
    This script is in the public domain, free from copyrights or restrictions.

VERSION
    $Id$
"""
import arcpy
from arcpy.sa import *
import os, sys, traceback
import re
from datetime import date
from dateutil.relativedelta import relativedelta


# To avoid overwriting outputs, change overwriteOutput option to False.
arcpy.env.overwriteOutput = True


# Check if there is DRY Month data in output folder
def create_DM_List(_DM_folder):
    print("start reading existing DRY Month Dataset....")
    print("looking for file with naming wld_cli_SPEI_dry_YYYYMMDD")
    
    DM_Date_List=[]
    
    for DM_Data in os.listdir(_DM_folder):
        if DM_Data.endswith(".tif") or DM_Data.endswith(".tiff"):
            print("found " + DM_Data + " in the DRY Month folder")
            
            parse_String = DM_Data.split('_')
            DM_Data_Date = parse_String[4]
            DM_Date_List.append(DM_Data_Date)
    
    return DM_Date_List


# Check if there is Consecutive DRY Month data in output folder
def create_CDM_List(_CDM_folder):
    print("start reading existing Consecutive DRY Month Dataset....")
    print("looking for file with naming wld_cli_SPEI_dry_YYYYMMDD")
    
    CDM_Date_List=[]
    
    for CDM_Data in os.listdir(_CDM_folder):
        if CDM_Data.endswith(".tif") or CDM_Data.endswith(".tiff"):
            print("found " + CDM_Data + " in the Consecutive DRY Month folder")
            
            parse_String = CDM_Data.split('_')
            CDM_Data_Date = parse_String[4]
            CDM_Date_List.append(CDM_Data_Date)
    
    return CDM_Date_List


# Check input data
def create_monthly_List(_tif_folder):
    print("start reading list of monthly SPEI data....")
    print("looking for file with naming wld_cli_SPEI_gamma_12_terraclimate_YYYY-MM-DD")
    
    Monthly_Date_List=[]
    
    for Monthly_Data in os.listdir(_tif_folder):
        
        if Monthly_Data.endswith(".tif") or Monthly_Data.endswith(".tiff"):
            print("found " + Monthly_Data+ " in the monthly SPEI folder")
            
            finds = re.findall(r'[^\d](\d{4}[^\d]\d{2}[^\d]\d{2})([^\d]|$)', Monthly_Data)
            if not finds:
                raise Exception('YYYY.MM.DD pattern not found')
            ymd = re.sub(r'[^\d]+', '', finds[0][0])
            
            Monthly_Data_Date = ymd            
            Monthly_Date_List.append(Monthly_Data_Date)
    
    return sorted(Monthly_Date_List)


# Execute first Dry condition
def execute_first_DM(_tiffolder, _DMFolder, threshold):
    # Spatial reference WGS-84
    sr = arcpy.SpatialReference(4326)
    print("looking at the first monthly SPEI data in tif folder...")
    
    monthly_list = create_monthly_List(_tiffolder)
    first_date = min(monthly_list)
    print("execute first SPEI data from date "+first_date)
    
    first_data_name = 'wld_cli_SPEI_gamma_12_terraclimate_{0}-{1}-{2}.tif'.format(first_date[0:4], first_date[4:6], first_date[6:8])
    first_monthly_data = os.path.join(_tiffolder, first_data_name)
    monthly_Date = date(int(first_date[0:4]), int(first_date[4:6]), int(first_date[6:8]))
    dry_date = monthly_Date + relativedelta(months=1)
    print("creating dry data "+str(dry_date)+ " from monthly SPEI data from "+str(monthly_Date))
    
    DMyear = str(dry_date.year)
    DMmonth = str(dry_date.month)
    DMday = str(dry_date.day)
    print(str(dry_date))
    
    DMFilename = 'wld_cli_SPEI_dry_{0}{1}{2}.tif'.format(DMyear.zfill(4), DMmonth.zfill(2), DMday.zfill(2))
    print("Processing "+DMFilename)
    
    arcpy.CheckOutExtension("spatial")
    
    outCon = Con(Raster(first_monthly_data) < Float(threshold), 1, 0)
    outCon.save(os.path.join(_DMFolder, DMFilename))
    arcpy.DefineProjection_management(os.path.join(_DMFolder, DMFilename), sr)
    
    arcpy.CheckInExtension("spatial")
    print("file " + DMFilename + " is created")


# Execute first Dry condition
def execute_first_CDM(_tiffolder, _CDMFolder, threshold):
    # Spatial reference WGS-84
    sr = arcpy.SpatialReference(4326)
    print("looking at the first monthly SPEI data in tif folder...")
    
    monthly_list = create_monthly_List(_tiffolder)
    first_date = min(monthly_list)
    print("execute first SPEI data from date "+first_date)
    
    first_data_name = 'wld_cli_SPEI_gamma_12_terraclimate_{0}-{1}-{2}.tif'.format(first_date[0:4], first_date[4:6], first_date[6:8])
    first_monthly_data = os.path.join(_tiffolder, first_data_name)
    monthly_Date = date(int(first_date[0:4]), int(first_date[4:6]), int(first_date[6:8]))
    dry_date = monthly_Date + relativedelta(months=1)
    print("creating dry data "+str(dry_date)+ " from monthly SPEI data from "+str(monthly_Date))
    
    CDMyear = str(dry_date.year)
    CDMmonth = str(dry_date.month)
    CDMday = str(dry_date.day)
    print(str(dry_date))
    
    CDMFilename = 'wld_cli_SPEI_dry_{0}{1}{2}.tif'.format(CDMyear.zfill(4), CDMmonth.zfill(2), CDMday.zfill(2))
    print("Processing "+CDMFilename)
    
    arcpy.CheckOutExtension("spatial")
    
    outCon = Con(Raster(first_monthly_data) < Float(threshold), 1, 0)
    outCon.save(os.path.join(_CDMFolder, CDMFilename))
    arcpy.DefineProjection_management(os.path.join(_CDMFolder, CDMFilename), sr)
    
    arcpy.CheckInExtension("spatial")
    print("file " + CDMFilename + " is created")


# Execute next DRY Month data
def execute_DM(_lastdate, _tiffolder, _DM_folder, threshold):
    # Spatial reference WGS-84
    sr = arcpy.SpatialReference(4326)
    
    date_formatted = date(int(_lastdate[0:4]), int(_lastdate[4:6]), int(_lastdate[6:8]))
    last_dryname = 'wld_cli_SPEI_dry_{0}'.format(_lastdate)
    last_dryfile = os.path.join(_DM_folder, last_dryname)
    next_monthlyname = 'wld_cli_SPEI_gamma_12_terraclimate_{0}-{1}-{2}.tif'.format(_lastdate[0:4], _lastdate[4:6], _lastdate[6:8])
    next_monthlydata = os.path.join(_tiffolder, next_monthlyname)
    
    if arcpy.Exists(next_monthlydata):
        print("next monthly data is available...")
        print("start processing next DRY Month...")
        
        new_dry_date = date_formatted + relativedelta(months=1)
        DMyear1 = str(new_dry_date.year)
        DMmonth1 = str(new_dry_date.month)
        DMday1 = str(new_dry_date.day)
        new_dry_name = 'wld_cli_SPEI_dry_{0}{1}{2}.tif'.format(DMyear1.zfill(4), DMmonth1.zfill(2), DMday1.zfill(2))
        print("Processing DRY Month from "+last_dryfile+" and "+next_monthlydata)
        
        arcpy.CheckOutExtension("spatial")
        
        outDMCon = Con(Raster(next_monthlydata) < Float(threshold), 1, 0)
        outDMCon.save(os.path.join(_DM_folder, new_dry_name))
        arcpy.DefineProjection_management(os.path.join(_DM_folder, new_dry_name), sr)
        
        arcpy.CheckInExtension("spatial")
        print("DRY Month File "+new_dry_name+" is created")
    
    else:
        print("next monthly data is not available. Exit...")


# Execute next Consecutive DRY Month data
def execute_CDM(_lastdate, _tiffolder, _CDM_folder, threshold):
    # Spatial reference WGS-84
    sr = arcpy.SpatialReference(4326)
    
    date_formatted = date(int(_lastdate[0:4]), int(_lastdate[4:6]), int(_lastdate[6:8]))
    last_dryname = 'wld_cli_SPEI_dry_{0}'.format(_lastdate)
    last_dryfile = os.path.join(_CDM_folder, last_dryname)
    next_monthlyname = 'wld_cli_SPEI_gamma_12_terraclimate_{0}-{1}-{2}.tif'.format(_lastdate[0:4], _lastdate[4:6], _lastdate[6:8])
    next_monthlydata = os.path.join(_tiffolder, next_monthlyname)
    
    if arcpy.Exists(next_monthlydata):
        print("next monthly data is available...")
        print("start processing next Consecutive DRY Month...")
        
        new_dry_date = date_formatted + relativedelta(months=1)
        CDMyear1 = str(new_dry_date.year)
        CDMmonth1 = str(new_dry_date.month)
        CDMday1 = str(new_dry_date.day)
        new_dry_name = 'wld_cli_SPEI_dry_{0}{1}{2}.tif'.format(CDMyear1.zfill(4), CDMmonth1.zfill(2), CDMday1.zfill(2))
        print("Processing Consecutive DRY Month from "+last_dryfile+" and "+next_monthlydata)
        
        arcpy.CheckOutExtension("spatial")
        
        outCDMCon = Con(Raster(next_monthlydata) < Float(threshold), Raster(last_dryfile)+1, 0)
        outCDMCon.save(os.path.join(_CDM_folder, new_dry_name))
        arcpy.DefineProjection_management(os.path.join(_CDM_folder, new_dry_name), sr)
        
        arcpy.CheckInExtension("spatial")
        print("Consecutive DRY Month File "+new_dry_name+" is created")
    
    else:
        print("next monthly data is not available. Exit...")


# Run the script
def create_DM(_DM_folder, _tiffolder, threshold):

    DM_Date_List = create_DM_List(_DM_folder)
    Monthly_list = create_monthly_List(_tiffolder)
    
    # if there is no DRY data, creating new DRY data
    if len(DM_Date_List)==0:
        print("No DRY Month data found...")
        print("Creating first DRY Month data...")
        
        execute_first_DM(_tiffolder, _DM_folder, threshold)
        DM_Date_List = create_DM_List(_DM_folder)
    
    # if there is DRY Month data
    print("DRY Month data found. Looking for latest DRY Month data...")
    
    #Check last DRY Month available
    last_date = max(DM_Date_List)

    #Check last monthly data availabke
    max_monthly_date = max(Monthly_list)
    last_DM_date = date(int(last_date[0:4]), int(last_date[4:6]), int(last_date[6:8]))
    last_monthly_date = date(int(max_monthly_date[0:4]), int(max_monthly_date[4:6]), int(max_monthly_date[6:8]))
    
    # process DRY Month to every monthly data available after last DRY Month data
    while last_monthly_date + relativedelta(months=1) > last_DM_date:

        execute_DM(last_date, _tiffolder, _DM_folder, threshold)

        last_DM_date=last_DM_date+relativedelta(months=1)
        DMyear2 = str(last_DM_date.year)
        DMmonth2 = str(last_DM_date.month)
        DMday2 = str(last_DM_date.day)
        last_date='{0}{1}{2}.tif'.format(DMyear2.zfill(4), DMmonth2.zfill(2), DMday2.zfill(2))

    print("All DRY Month data is available")


# Run the script
def create_CDM(_CDM_folder, _tiffolder, threshold):

    CDM_Date_List = create_CDM_List(_CDM_folder)
    Monthly_list = create_monthly_List(_tiffolder)
    
    # if there is no DRY data, creating new DRY data
    if len(CDM_Date_List)==0:
        print("No Consecutive DRY Month data found...")
        print("Creating first Consecutive DRY Month data...")
        
        execute_first_CDM(_tiffolder, _CDM_folder, threshold)
        CDM_Date_List = create_CDM_List(_CDM_folder)
    
    # if there is Consecutive DRY Month data
    print("Consecutive DRY Month data found. Looking for latest Consecutive DRY Month data...")
    
    #Check last Consecutive DRY Month available
    last_date = max(CDM_Date_List)

    #Check last monthly data availabke
    max_monthly_date = max(Monthly_list)
    last_CDM_date = date(int(last_date[0:4]), int(last_date[4:6]), int(last_date[6:8]))
    last_monthly_date = date(int(max_monthly_date[0:4]), int(max_monthly_date[4:6]), int(max_monthly_date[6:8]))
    
    # process Consecutive DRY Month to every monthly data available after last Consecutive DRY Month data
    while last_monthly_date + relativedelta(months=1) > last_CDM_date:

        execute_CDM(last_date, _tiffolder, _CDM_folder, threshold)

        last_CDM_date=last_CDM_date+relativedelta(months=1)
        CDMyear2 = str(last_CDM_date.year)
        CDMmonth2 = str(last_CDM_date.month)
        CDMday2 = str(last_CDM_date.day)
        last_date='{0}{1}{2}.tif'.format(CDMyear2.zfill(4), CDMmonth2.zfill(2), CDMday2.zfill(2))

    print("All Consecutive DRY Month data is available")


# Execute sum of DRY Month
def execute_SUM(output_folder, folder_to_extract):
    
    listoffile = []

    for data in os.listdir(folder_to_extract):
        if data.endswith(".tif"):
            listoffile.append(os.path.join(folder_to_extract, data))
    print("data to calculate is "+str(len(listoffile)))
    print("start running cell statistics to find total number of DRY Month in 1958-2020.....")
    
    arcpy.CheckOutExtension("spatial")
    
    sum_data_filename = 'wld_cli_SPEI_dry_duration_total_1958_2020.tif'
    sum_data = arcpy.sa.CellStatistics(listoffile, "SUM", "DATA")
    sum_data.save(os.path.join(output_folder, sum_data_filename))
    print(sum_data_filename + ' is succesfully created')
    
    arcpy.CheckInExtension("spatial")


# Execute max of Consective DRY Month
def execute_MAX(output_folder, folder_to_extract):
    
    listoffile = []

    for data in os.listdir(folder_to_extract):
        if data.endswith(".tif"):
            listoffile.append(os.path.join(folder_to_extract, data))
    print("data to calculate is "+str(len(listoffile)))
    print("start running cell statistics to find maximum Consecutive DRY Month in 1958-2020.....")
    
    arcpy.CheckOutExtension("spatial")
    
    max_data_filename = 'wld_cli_SPEI_dry_duration_max_1958_2020.tif'
    max_data = arcpy.sa.CellStatistics(listoffile, "MAXIMUM", "DATA")
    max_data.save(os.path.join(output_folder, max_data_filename))
    print(max_data_filename + ' is succesfully created')
    
    arcpy.CheckInExtension("spatial")


# Let's go!
if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"X:\ArcGIS_TEMP\Scratch.gdb", \
        workspace=r"X:\ArcGIS_TEMP\Default.gdb"):
	# Run the function (output folder, input folder, threshold)
        create_CDM('Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\consecutive_dry_month',\
            'Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\gamma',-1.2)
        # Run the function (output folder, input folder, threshold)
        create_DM('Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\dry_month',\
            'Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\gamma',-1.2)
	# Run the function (output folder, input folder)
        execute_MAX('Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\consecutive_dry_month_max',\
            'Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\consecutive_dry_month')
        # Run the function (output folder, input folder)
        execute_SUM('Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\dry_month_total',\
            'Z:\\Temp\\TERRACLIMATE\\SPEI\\Outputs\\SPEI-12\\geotiff\\dry_month')
