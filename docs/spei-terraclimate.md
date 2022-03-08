# SPEI using TerraClimate data

This section will explain on how to download TerraClimate's precipitation (ppt) and potential evapotranspiration (pet) monthly data in netCDF format and prepare it as input for SPEI calculation.

This step-by-step guide was tested using Mac mini Server - Late 2012, 2.3 GHz Quad-Core Intel Core i7, 16 GB 1600 MHz DDR3, running on macOS Catalina 10.15.7 and Windows 10 with Windows Subsystem for Linux enabled running on Parallels Desktop.

## 0. Working Directory

For this tutorial, we are working on these folder `/Users/gost/temp/terraclimate/spei/` (applied to Mac/Linux machine) or `Z:/temp/terraclimate/spei/` (applied to Windows machine) directory. I have some folder inside this directory:

1. `downloads`
	1. `ppt`
		1. `nc_original`
		2. `nc_merge`
		3. `nc_tiles`
		4. `nc_subset`
		5. `nc_llt` Place to put netCDF's ppt data that will use as an input
	2. `pet`
		1. `nc_original`
		2. `nc_merge`
		3. `nc_tiles`
		4. `nc_subset`
		5. `nc_llt` Place to put netCDF's pet data that will use as an input

	Place to put downloaded TerraCLimate data, and pre-process temporary files.

2. `output` 
	1. `nc_original` Output folder for SPEI calculation
		1. `gamma`
		2. `pearson`
	2. `nc_tll` Temporary for nc files from NCO arrange dimension process
	3. `nc_merge` Merging nc from separate tiles into single global layer (if you are following the global analysis procedures)
	4. `geotiff`
		1. `gamma` Final output of SPEI, generate by CDO and GDAL

Feel free to use your own preferences for this setting/folder arrangements.


## 1. Preparing input

SPEI requires monthly precipitation and potential evapotranspiration data, for better result, SPEI required minimum 30-years of data.

If you are prefer to use your own dataset also fine, you can still follow this guideline and adjust some steps and code related to filename, unit, format and structure.


### 1.1. Input requirement

The [climate-indices](https://pypi.org/project/climate-indices/) python package enables the user to calculate SPEI using any gridded netCDF dataset. However, there are certain requirements for input files that vary based on input type.

- Precipitation and potential evapotranspiration unit must be written as `millimeters`, `millimeter`, `mm`, `inches`, `inch` or `in`.

- Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL). 

- If your study area are big, it's better to prepare all the data following this dimension order: `lat`, `lon`, `time` as all the data will force following this order during SPEI calculation by NCO module. Let say you only prepare the data as is (leaving the order to `lat`, `lon`, `time`), it also acceptable but it will required lot of memory to use re-ordering the dimension, and usually NCO couldn't handle all the process and failed.


### 1.2. Download TerraClimate data

- There are 2 files contains link for downloading `ppt` ([https://github.com/worldbank/GOST_Climate/blob/main/downloads/ppt/nc_original/data_ppt.sh](https://github.com/worldbank/GOST_Climate/blob/main/downloads/ppt/nc_original/data_ppt.sh) and `pet` ([https://github.com/worldbank/GOST_Climate/blob/main/downloads/pet/nc_original/data_pet.sh](https://github.com/worldbank/GOST_Climate/blob/main/downloads/pet/nc_original/data_pet.sh)), the folder location are exactly the same with the working directory above. 

- Download both files and put it in the same location with your working directory.

- Navigate to `downloads/terraclimate/ppt/nc_original` and `downloads/terraclimate/pet/nc_original`folder in the working directory. Download using `wget` all TerraClimate in netCDF format from Jan 1958 to Dec 2020 (this is lot of data, `ppt` +- 7.7GB and `pet` +- 6.4GB, please make sure you have bandwidth and unlimited data package). Paste and Enter below script in your Terminal.

	If you are in `downloads/terraclimate/ppt/nc_original` then execute below command

	```bash
	sh data_ppt.sh
	```
	If you are in `downloads/terraclimate/pet/nc_original` then execute below command

	```bash
	sh data_pet.sh
	```

> **_NOTE:_**  
> This guideline provide example on how to use CDO and NCO to do some data extraction process,
you can choose which one is suits you.


### 1.3. Clip data using a bounding box based on area of interest and merge netCDFs into single netCDF

- Clip your area of interest using bounding box. We will use Sao Tome and Principe (STP) as the example case.
	
	Example: (STP) bounding box with format `lon1`,`lon2`,`lat1`,`lat2` is `5.75`,`8.05`,`-0.35`,`2.15`

	Precipitation: Navigate your location to `/downloads/ppt/nc_original`

	CDO script:

	``` bash
	for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done
	```

	NCO script:

	``` bash
	for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done
	```

	Potential Evapotranspiration: Navigate your location to `/downloads/pet/nc_original`

	CDO script:

	``` bash
	for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done
	```

	NCO script:

	``` bash
	for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done
	```

- Merge all annual netcdf in a folder into single netcdf.

	Precipitation: make sure you are in `/downloads/ppt/nc_subset`

	CDO script:

	```bash
	cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc
	```

	NCO script:
	Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files.

	```bash
	for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done
	```

	Then we are ready to concatenate it.

	```bash
	ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc
	```

	Potential Evapotranspiration: make sure you are in `/downloads/pet/nc_subset`

	CDO script:

	```bash
	cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc
	```

	NCO script:
	Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files.

	```bash
	for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done
	```

	Then we are ready to concatenate it.

	```bash
	ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc
	```


### 1.4. Check variable and attribute
As explain in Step 1.1. Input requirement above, we need to check the variable and attribute on above result to make sure all meet the requirements. 

- Navigate to `/downloads/ppt/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_ppt_1958_2020.nc
	```

	![ncdump ppt](./img/ncdump-ppt.png)

- Navigate to `/downloads/pet/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_pet_1958_2020.nc
	```

	![ncdump pet](./img/ncdump-pet.png)

- As you can see from above picture, all the requirement is completed: unit is in `mm`, order dimension for each variables is `lat`, `lon`, `time`, and `time` dimension is in `UNLIMITED`. Once this has completed, the dataset can be used as input to `climate-indices` package for computing SPEI. 


## 2. Calculate SPEI

Please make sure below points:

- [x] You are still inside `climate_indices` environment to start working on SPEI calculation. 
- [x] Variable name on precipitation `--var_name_precip`, usually TerraClimate data use `ppt` as name while other precipitation data like CHIRPS using `precip` and IMERG using `precipitation` as a variable name. To make sure, check using command `ncdump -h file.nc` then adjust it in SPEI script if needed.
- [x] Variable name on potential evapotranspiration `--var_name_pet`, usually TerraClimate data use `pet` as name.
- [x] Precipitation and potential evapotranspiration unit must be written as `millimeters`, `milimeter`, `mm`, `inches`, `inch` or `in`.
- [x] Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL).

Let's start the calculation!

- In your Terminal, run the following code.

	``` bash
	process_climate_indices --index spei --periodicity monthly --netcdf_precip /Users/gost/temp/terraclimate/spei/downloads/ppt/nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc --var_name_precip ppt --netcdf_pet /Users/gost/temp/terraclimate/spei/downloads/pet/nc_merge/stp_cli_terraclimate_pet_1958_2020.nc --var_name_pet pet --output_file_base /Users/gost/temp/terraclimate/spei/output/nc_original/spt_cli_spei --scales 1 2 3 6 9 12 18 24 36 48 60 72 --calibration_start_year 1958 --calibration_end_year 2020 --multiprocessing all
	```

- Above code is example for calculating SPEI 1 to 72-months. It's ok if you think you only need some of them. Example: you are interested to calculate SPEI 1 - 3-months or SPEI 12-months, then adjust above code into `--scales 1 2 3` or `--scales 12`.

- The above command will compute SPEI (both gamma and Pearson Type III distributions) from monthly precipitation dataset and potential evapotranspiration, and the calibration period used will be Jan-1958 through Dec-2020. The index will be computed at `1`,`2`,`3`,`6`,`9`,`12`,`18`,`24`,`36`,`48`,`60` and `72-month` timescales. The output files will be <`out_dir>/stp_cli_spei_gamma_xx.nc`, and `<out_dir>/stp_cli_spei_pearson_xx.nc`.

	The output files will be:

	Gamma

	1. 1-month: `/output/nc_original/stp_cli_spei_gamma_01.nc`</br>
	2. 2-month: `/output/nc_original/stp_cli_spei_gamma_02.nc`</br>
	3. 3-month: `/output/nc_original/stp_cli_spei_gamma_03.nc`</br>
	4. 6-month: `/output/nc_original/stp_cli_spei_gamma_06.nc`</br>
	5. 9-month: `/output/nc_original/stp_cli_spei_gamma_09.nc`</br>
	6. 12-month: `/output/nc_original/stp_cli_spei_gamma_12.nc`</br>
	7. 18-month: `/output/nc_original/stp_cli_spei_gamma_18.nc`</br>
	8. 24-month: `/output/nc_original/stp_cli_spei_gamma_24.nc`</br>
	9. 36-month: `/output/nc_original/stp_cli_spei_gamma_36.nc`</br>
	10. 48-month: `/output/nc_original/stp_cli_spei_gamma_48.nc`</br>
	11. 60-month: `/output/nc_original/stp_cli_spei_gamma_60.nc`</br>
	12. 72-month: `/output/nc_original/stp_cli_spei_gamma_72.nc`</br>

	Pearson

	1. 1-month: `/output/nc_original/stp_cli_spei_pearson_01.nc`</br>
	2. 2-month: `/output/nc_original/stp_cli_spei_pearson_02.nc`</br>
	3. 3-month: `/output/nc_original/stp_cli_spei_pearson_03.nc`</br>
	4. 6-month: `/output/nc_original/stp_cli_spei_pearson_06.nc`</br>
	5. 9-month: `/output/nc_original/stp_cli_spei_pearson_09.nc`</br>
	6. 12-month: `/output/nc_original/stp_cli_spei_pearson_12.nc`</br>
	7. 18-month: `/output/nc_original/stp_cli_spei_pearson_18.nc`</br>
	8. 24-month: `/output/nc_original/stp_cli_spei_pearson_24.nc`</br>
	9. 36-month: `/output/nc_original/stp_cli_spei_pearson_36.nc`</br>
	10. 48-month: `/output/nc_original/stp_cli_spei_pearson_48.nc`</br>
	11. 60-month: `/output/nc_original/stp_cli_spei_pearson_60.nc`</br>
	12. 72-month: `/output/nc_original/stp_cli_spei_pearson_72.nc`</br>

Parallelization will occur utilizing all CPUs.

When the SPEI calculation completed, move arrange all the output by moving SPEI files with gamma to `gamma`folder and with pearson to `pearson` folder.

For the translation to GeoTIFF as a final output, we only use SPEI gamma version.


## 3. Visualize the result using Panoply

Let see the result.

- From the `/output/nc_original/gamma` directory, right-click file `stp_cli_spei_gamma_12.nc` and Open With Panoply.

	If you are not following the tutorial but interested to see the file, you can download this file from this link: []() 

- From the Datasets tab select `spei_gamma_12_month` and click Create Plot

- In the Create Plot window select option Georeferenced Longitude-Latitude.

- When the Plot window opens:

	- Array tab: Change the time into `717` to view data on `1 September 2019`
	- Scale tab: Change value on Min `-3.09`, Max `3.09`, Major `6`, Color Table `CB_RdBu_09.cpt`
	- Map tab: Change value on Center on Lon `7.0` Lat `1.0`, then Zoom in the map through menu-editor Plot > Zoom - Plot In few times until Sao Tome and Principe appear proportionally. Set grid spacing `1.0` and Labels on every grid lines.
	- Overlays tab: Change `Overlay 1` to `MWDB_Coasts_Countries_1.cnob`

	![SPEI-12](./img/stp-spei-12.png)


## 4. Convert the result to GeoTIFF

We need CDO to do a conversion of the result into GeoTIFF format, and CDO required the variable should be in `time`,`lat`,`lon`, while the output from SPEI: `stp_cli_spei_gamma_x_month.nc` in `lat`,`lon`,`time`, you can check this via `ncdump -h stp_cli_spei_gamma_12.nc`

- Navigate your Terminal to folder `/output/nc_original/gamma/`

- Let's re-order the variables into `time`,`lat`,`lon` using `ncpdq` command from NCO and save the result to folder `/output/nc_tll/STP/`

	``` bash
	ncpdq -a time,lat,lon stp_cli_spei_gamma_12.nc ../../../output/nc_tll/STP/tp_cli_spei_gamma_12.nc
	```

- Navigate your Terminal to folder `/output/nc_tll/STP/`

- Check result and metadata to make sure everything is correct.

	``` bash
	ncdump -h stp_cli_spei_gamma_12.nc
	```

- Then convert all `stp_cli_spei_gamma_12.nc` value into GeoTIFF with `time` dimension information as the filename using CDO and GDAL. Usually the geotiff image will not have projection information, so we will add that information via the script: `-a_ullr ulx uly lrx lry -a_srs EPSG:4326`

- Execute below script and save the result to folder `/output/geotiff/gamma/STP/SPEI-12`

	``` bash
	for t in `cdo showdate stp_cli_spei_gamma_12.nc`; do
	    cdo seldate,$t stp_cli_spei_gamma_12.nc dummy.nc     
	    gdal_translate -of GTiff -a_ullr 5.75 2.15 8.05 -0.35 -a_srs EPSG:4326 -co COMPRESS=LZW -co PREDICTOR=1 dummy.nc ../../geotiff/gamma/STP/SPEI-12/stp_cli_terraclimate_spei12.$t.tif
	done
	```

- Next, you can continue to translate other SPEI files.

Congrats, now you are able to calculate SPEI based on monthly rainfall in netCDF and translate the output into GeoTIFF format.


## 5. Global SPEI data

Global SPEI-12 data using TerraClimate has been computed, other SPEI for different time period will follow. The monthly SPEI data is available in GeoTIFF format at DEC S3 bucket: `s3://wbgdecinternal-ntl/climate/products/spei-terraclimate/spei-12/geotiff`


### 5.1. Example output

Below is the example of global SPEI-12 as of December 2020, generated by GOST team.

![GOST_SPEI12_Dec2020](./img/gost-global-spei12-20201201.png)


### 5.2. Comparison with other data provider

**SPEI Global Drought Monitor**

Santiago Begueria and friend from Spanish National Research Council who invented SPEI, released the [SPEI Global Drought Monitor](https://spei.csic.es/index.html) which offers near real-time information about drought conditions at the global scale, with a 1 degree spatial resolution and a monthly time resolution.

Link for SPEI 12-month, December 2020 from Global Drought Monitor - [https://spei.csic.es/map/maps.html#months=4#month=11#year=2020](https://spei.csic.es/map/maps.html#months=4#month=11#year=2020)

![GDM_SPEI12_Dec2020](./img/gdm-global-spei12-20201201.png)

**Climate Engine**

[**Climate Engine**](http://climateengine.org) is a free web application powered by Google Earth Engine that can be used to create on-demand maps and charts from publicly available satellite and climate data using a standard web browser. Climate Engine allows users to analyze and interact with climate and earth observations for decision support related to drought, water use, agricultural, wildfire, and ecology.

One of the product that could generate easily using Climate Engine is SPEI and using TerraClimate data. Link [https://climengine.page.link/yMtH](https://climengine.page.link/yMtH)

![ClimateEngine_SPEI12_Dec2020](./img/climengine-global-spei12-20201201.png)


## 6. Reference

1. [https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-evapotranspiration-index-spei](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-evapotranspiration-index-spei)
2. [https://spei.csic.es](https://spei.csic.es)
3. [http://www.climatologylab.org/terraclimate.html](http://www.climatologylab.org/terraclimate.html)
4. [https://pypi.org/project/climate-indices/](https://pypi.org/project/climate-indices/)
5. [https://climate-indices.readthedocs.io/en/latest/](https://climate-indices.readthedocs.io/en/latest/)
6. [https://code.mpimet.mpg.de/projects/cdo](https://code.mpimet.mpg.de/projects/cdo)
7. [http://nco.sourceforge.net](http://nco.sourceforge.net)
8. [https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-gpm-imerg-reanalysis-assessing-extreme-dry-and-wet](https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-gpm-imerg-reanalysis-assessing-extreme-dry-and-wet)
