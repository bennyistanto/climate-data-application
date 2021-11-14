# SPEI using TerraClimate data

This section will explain on how to download TerraClimate's precipitation (ppt) and potential evapotranspiration (pet) monthly data in netCDF format and prepare it as input for SPEI calculation.

This step-by-step guide was tested using Mac mini Server - Late 2012, 2.3 GHz Quad-Core Intel Core i7, 16 GB 1600 MHz DDR3, running on macOS Catalina 10.15.7 and Windows 10 with Windows Subsystem for Linux enabled running on Parallels Desktop.

## 0. Working Directory

For this tutorial, I am working on these folder `/Users/bennyistanto/Temp/TerraClimate/SPEI/` (applied to Mac/Linux machine) or `Z:/Temp/TerraClimate/SPEI/` (applied to Windows machine) directory. I have some folder inside this directory:

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

2. `outputs` 
	1. `nc_original` Output folder for SPEI calculation
		1. `gamma`
		2. `pearson`
	2. `nc_tll` Temporary for nc files from NCO arrange dimension process
	3. `nc_merge` Merging nc from separate tiles into single global layer (if you are following the global analysis procedures)
	4. `geotiff`
		1. `gamma` Final output of SPEI, generate by CDO and GDAL

Feel free to use your own preferences for this setting/folder arrangements.


## 1. Software Requirement

If you encounter a problem, please look for a online solution. The installation and configuration described below is mostly performed using a bash shell on macOS. Windows users will need to install and configure a bash shell in order to follow the usage shown below. Try to use [Windows Subsystem for Linux](#enable-the-windows-subsytem-for-linux) for this purpose.


### macOS/Linux

#### Installing software for macOS/Linux

If you are new to using Bash refer to the following lessons with Software Carpentry: [http://swcarpentry.github.io/shell-novice/](http://swcarpentry.github.io/shell-novice/)

- If you don't have [**Homebrew**](https://brew.sh), you can install it by pasting below code in your macOS/Linux terminal.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Install `wget` (for downloading data). Use Hombrew to install it by pasting below code in your macOS terminal.

```bash
brew install wget
```

- Download and install [Panoply Data Viewer](https://www.giss.nasa.gov/tools/panoply/) from [NASA GISS](https://www.giss.nasa.gov/tools/panoply/download/) on your machine for [macOS](https://www.giss.nasa.gov/tools/panoply/download/PanoplyMacOS-4.12.2.dmg) or [Linux](https://www.giss.nasa.gov/tools/panoply/download/PanoplyJ-4.12.2.zip).

- Download and install [Anaconda Python](https://www.anaconda.com/products/individual) on your machine for [macOS](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg) or [Linux](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh).

	- Follow Installing Anaconda on [macOS](https://docs.anaconda.com/anaconda/install/mac-os/) guideline and for [Linux](https://docs.anaconda.com/anaconda/install/linux/)


### Windows

#### Enable the Windows Subsytem for Linux

If you are using Windows machine, it's recomended to follow below step. You will experience an error during SPI calculation cause by `NCO` if you use standard Windows 10 and not using Windows Subsytem for Linux. 

Guideline below are specific for Windows 10. If you are using Windows Server 2019, please follow [Windows Server Installation Guide](https://docs.microsoft.com/en-us/windows/wsl/install-on-server)
    
Reference: [https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

You must first enable the "Windows Subsystem for Linux - WSL" optional feature before installing any Linux distributions on Windows.

#### Installing software for Windows

If you have a Bash shell already installed on your Windows OS (e.g. Ubuntu Bash) you can use that for the exercise, but it must be a Bash shell

If you are new to using Bash refer to the following lessons with Software Carpentry: [http://swcarpentry.github.io/shell-novice/](http://swcarpentry.github.io/shell-novice/)

- If you don't have [**Homebrew**](https://brew.sh), you can install it by pasting below code in your WSL Ubuntu terminal.

```bash
bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

- Install `wget` (for downloading data). Use Hombrew to install it by pasting below code in your WSL Ubuntu  terminal.

```bash
brew install wget
```

- Download and install [Panoply Data Viewer](https://www.giss.nasa.gov/tools/panoply/) from [NASA GISS](https://www.giss.nasa.gov/tools/panoply/download/) on your machine: [Windows](https://www.giss.nasa.gov/tools/panoply/download/PanoplyWin-4.12.2.zip).

- Download and install [Anaconda Python](https://www.anaconda.com/products/individual) on your WSL Ubuntu Linux: [Ubuntu Linux on WSL](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh).

	`climate-indices` python package used for SPI calculation is rely on [**netCDF Operator (NCO)**](http://nco.sourceforge.net) and pyNCO wrapper sometimes produce an error in Windows. That's the reason why we will use Anaconda for Linux if you are using Windows machine.

Reference: [https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da](https://gist.github.com/kauffmanes/5e74916617f9993bc3479f401dfec7da)

- Go to [https://repo.anaconda.com/archive/](https://repo.anaconda.com/archive/) to find the list of Anaconda releases
- Select the release you want. I have a 64-bit computer, so I chose the latest release ending in `x86_64.sh`. If I had a 32-bit computer, I'd select the `x86.sh` version. If you accidentally try to install the wrong one, you'll get a warning in the terminal. I chose `Anaconda3-2020.11-Linux-x86_64.sh`.
- From the terminal run `wget https://repo.anaconda.com/archive/[YOUR VERSION]`. Example: 

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
```

- After download process completed, Run the installation script: `bash Anaconda[YOUR VERSION].sh` 

```bash
bash Anaconda3-2020.11-Linux-x86_64.sh
```

- Read the license agreement and follow the prompts to press Return/Enter to accept. Later will follow with question on accept the license terms, type `yes` and Enter. When asks you if you'd like the installer to prepend it to the path, press Return/Enter to confirm the location. Last question will be about initialize Anaconda3, type `yes` then Enter.
- Close the terminal and reopen it to reload .bash configs. It will automatically activate `base` environment.
- Deactivate `base` environment then set to `false` the confirguration of auto activate the `base` environment by typing

```bash
conda deactivate && conda config --set auto_activate_base false
```

- To test that it worked, `which python` in your Terminal. It should print a path that has anaconda in it. Mine is `/home/bennyistanto/anaconda3/bin/python`. If it doesn't have anaconda in the path, do the next step.
- Manually add the Anaconda bin folder to your PATH. To do this, I added `"export PATH=/home/bennyistanto/anaconda3/bin:$PATH"` to the bottom of my `~/.bashrc` file.
- Optionally install [**Visual Studio Code**](https://code.visualstudio.com) when prompted


## 2. Configure the python environment

The code for calculating SPEI is written in Python 3. It is recommended to use either the **Miniconda3** (minimal Anaconda) or **Anaconda3** distribution. The below instructions will be Anaconda specific (although relevant to any Python virtual environment), and assume the use of a bash shell.

A new Anaconda [environment](https://conda.io/docs/using/envs.html) can be created using the [conda](https://conda.io/docs/) environment management system that comes packaged with Anaconda. In the following examples, I’ll use an environment named `climate_indices` (any environment name can be used instead of `climate_indices`) which will be created and populated with all required dependencies through the use of the provided setup.py file.

This step must **only be done the first time**. Once the environment has been created there is no need to do it again.

- First, open your Terminal (in your macOS/Linux and Ubuntu Linux on WSL), create the Python environment with `python3.7` as default:

```bash
conda create -n climate_indices python=3.7
```

Proceed with `y`

- The environment created can now be ‘activated’:

```bash
conda activate climate_indices
```

- Install netCDF Operator ([NCO](http://nco.sourceforge.net/)), Climate Data Operator ([CDO](https://code.mpimet.mpg.de/projects/cdo)) from Max-Planck-Institut für Meteorologie and Geospatial Data Abstraction Library ([GDAL/OGR](https://gdal.org)) using `conda` and proceed with `y`.

```bash
conda install -c conda-forge nco cdo gdal
```

- Install [climate-indices](https://pypi.org/project/climate-indices/) package. Once the environment has been activated then subsequent Python commands will run in this environment where the package dependencies for this project are present. Now the package can be added to the environment along with all required modules (dependencies) via [pip](https://pip.pypa.io/en/stable/):

```bash
pip install climate-indices
```

## 3. Preparing input

SPEI requires monthly precipitation and potential evapotranspiration data, for better result, SPEI required minimum 30-years of data.

If you are prefer to use your own dataset also fine, you can still follow this guideline and adjust some steps and code related to filename, unit, format and structure.


### Input specification

The [climate-indices](https://pypi.org/project/climate-indices/) python package enables the user to calculate SPEI using any gridded netCDF dataset. However, there are certain specifications for input files that vary based on input type.

- Precipitation unit must be written as `millimeters`, `milimeter`, `mm`, `inches`, `inch` or `in`.

- Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL). 

- For this exercise, all the data will prepare following this dimension order: `lat`, `lon`, `time` as all the data will force following this order during SPEI calculation by NCO module.

### Download TerraClimate data

- There are 2 files contains link for downloading `ppt` ([https://github.com/bennyistanto/climate-data-application/blob/main/downloads/ppt/nc_original/data_ppt.sh](https://github.com/bennyistanto/climate-data-application/blob/main/downloads/ppt/nc_original/data_ppt.sh) and `pet` ([https://github.com/bennyistanto/climate-data-application/blob/main/downloads/pet/nc_original/data_pet.sh](https://github.com/bennyistanto/climate-data-application/blob/main/downloads/pet/nc_original/data_pet.sh)), the folder location are exactly the same with the working directory above. 
- Download both files and put it in the same location with your working directory.
- Navigate to `Downloads/TerraClimate/ppt/nc_original` and `Downloads/TerraClimate/pet/nc_original`folder in the working directory. Download using `wget` all TerraClimate in netCDF format from Jan 1958 to Dec 2020 (this is lot of data, `ppt` +- 7.7GB and `pet` +- 6.4GB, please make sure you have bandwidth and unlimited data package). Paste and Enter below script in your Terminal.

If you are in `Downloads/TerraClimate/ppt/nc_original` then execute below command

```bash
sh data_ppt.sh
```
If you are in `Downloads/TerraClimate/pet/nc_original` then execute below command

```bash
sh data_pet.sh
```

### Merge netCDFs into single netCDF

Merge all netcdf in a folder into single netcdf

```
cdo mergetime TerraClimate_*.nc TerraClimate_ppt_1958_2020.nc
```

### Clip data using a bounding box based on area of interest

I am providing example on how to use CDO and NCO to do some data extraction process, you can choose which one is suits you. In my opinion, NCO is faster than CDO, and NCO produce smaller size of output.

- Crop your area of interest using bounding box. We will use Sao Tome and Principe (STP) as the example case.
	Example: (STP) bounding box with format `lon1`,`lon2`,`lat1`,`lat2` is `5.75`,`8.05`,`-0.35`,`2.15`

Paste and Enter below code in your Terminal.

CDO script:

``` bash
cdo sellonlatbox,5.75,8.05,-0.35,2.15 TerraClimate_ppt_1958_2020.nc stp_cli_terraclimate_ppt_1958_2020.nc
```

NCO script:

``` bash
ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 TerraClimate_ppt_1958_2020.nc -O ../nc_subset/stp_cli_terraclimate_ppt_1958_2020.nc
```

- Let's read header contents of above result. Type and execute below code:

``` bash
ncdump -h stp_cli_terraclimate_ppt_1958_2020.nc
```