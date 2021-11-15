# Climate data and application

Mapping the extent of a natural hazard (e.g., assessing areas with a high risk) or disaster is a first step in disaster risk management and emergency response. Subsequently, exposure mapping enables the estimation of the impact of hazards or disasters, for example, regarding the number of affected inhabitants or infrastructure. 

This section describes in detail the methodology and analysis operations required for climate-based product data, to meet the user requirements of the World Bank at country, regional and global level. 

## Index
* [Climate Data](#climate-data)
	* [TerraClimate](#terraclimate)
		* [List datasets](#list-datasets)
		* [About the data](#labout-the-data)
		* [Downloads](#downloads)
	* [GPM IMERG](#gpm-imerg)
		* [List datasets](#list-datasets)
		* [About the data](#labout-the-data)
		* [Downloads](#downloads)
* [Climate Indices](#climate-indices)
	* [Standardized Precipitation-Evapotranspiration Index (SPEI)](#standardized-precipitation-evapotranspiration-index-spei)
		* [About the data](#labout-the-data)
		* [Symbology](#symbology)
	* [Consecutive Dry Days (CDD)](#consecutive-dry-days-cdd)
		* [How it works](#lhow-it-works)
		* [About the data](#labout-the-data)
		* [Symbology](#symbology)
* [How-to guides](#how-to-guides)

## Climate Data

The climate are varies by location and by time of year. Daily and monthly rainfall, monthly temperature and potential evapotranspiration are a few of the many datasets from various data providers found below.


### TerraClimate

[TerraClimate](http://www.climatologylab.org/terraclimate.html) is a dataset of monthly climate and climatic water balance for global terrestrial surfaces from 1958-2020. These data provide important inputs for ecological and hydrological studies at global scales that require high spatial resolution and time-varying data. All data have monthly temporal resolution and a 4-km (1/24th degree) spatial resolution. 

#### List datasets

**Primary Climate Variables:** Maximum temperature, minimum temperature, vapor pressure, precipitation accumulation, downward surface shortwave radiation, wind-speed

**Derived variables:** Reference evapotranspiration (ASCE Penman-Montieth), Runoff, Actual Evapotranspiration, Climate Water Deficit, Soil Moisture, Snow Water Equivalent, Palmer Drought Severity Index, Vapor pressure deficit

| Name  | Description  | Units |
|---|---|---|
| `aet`  | Actual Evapotranspiration, monthly total  | `mm` |
| `def`  | Climate Water Deficit, monthly total  | `mm` |
| `pet`  | Potential evapotranspiration, monthly total  | `mm` |
| `ppt`  | Precipitation, monthly total  | `mm` |
| `q`  | Runoff, monthly total  | `mm` |
| `soil`  | Soil Moisture, total column - at end of month  | `mm` |
| `srad`  | Downward surface shortwave radiation  | `W/m2` |
| `swe`  | Snow water equivalent - at end of month  | `mm` |
| `tmax`  | Max Temperature, average for month  | `°C` |
| `tmin`  | Min Temperature, average for month  | `°C` |
| `vap`  | Vapor pressure, average for month  | `kPa` |
| `ws`  | Wind speed, average for month  | `m/s` |
| `vpd`  | Vapor Pressure Deficit, average for month  | `kpa` |
| `PDSI`  | Palmer Drought Severity Index, at end of month  | `unitless` |

#### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays monthly climate datasets  |
| Variable  | Listed above  |
| Geographic coverage  | Global 90N-90S, 180W-180E |
| Spatial resolution  | 4-km at equator  |
| Temporal resolution  | monthly  |
| Format  | GeoTIFF  |
| Unit  | See list above  |

#### Downloads

Individual years download link: [http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data/catalog.html](http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data/catalog.html)

Also available at JNB Server Public Directory: J:\Data\GLOBAL\CLIMATE\TerraClimate


### GPM IMERG

The GPM is next-generation of the Tropical Rainfall Measuring Mission (TRMM - https://pmm.nasa.gov/TRMM). Like the TRMM, the GPM mission aims at providing uniformly calibrated precipitation estimates at a quasi-global scale by merging the measurements from its constellation of microwave and IR satellites. All GPM data sets including measurements obtained from each platform (Level 2) are available on the PMM site (https://pmm.nasa.gov/data-access). Among many GPM products, the Multi-satellitE Retrievals for GPM (IMERG) is most interesting to the users since it delivers the ‘best’ precipitation estimates by combining data obtained from all available microwave and infrared (IR) platforms of the GPM satellite constellation. 

IMERG is adjusted to GPCP monthly climatology zonally to achieve a bias profile that is considered reasonable. Multiple runs for different user requirements for latency and accuracy

1. “Early” – 4 hour (example application: flash flooding)
2. “Late” – 14 hour (crop forecasting)
3. “Final” – 3 months (research)

#### List datasets

Historical

| Timestep | Release | Period | Unit | Link |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Monthly | Final Run | Jun 2000 - Jul 2021 | mm/month | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/) |
| Daily | Final Run | 1 Jun 2000 - 31 Jul 2021 | mm/day | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDF.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDF.06/) |
| Daily | Early Run | 1 Jul 2000 - now | mm/day | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDE.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDE.06/) |
| Daily | Late Run | 1 Jul 2000 - now | mm/day | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDL.06/) |

Near-real time

| Timestep | Release | Period | Unit | Link |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 30-minutes | Final Run | 1 Jan 2020 - 31 Jul  2021 | mm/hour | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHH.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHH.06/) |
| 30-minutes | Early Run | 1 Jul 2020 - now | mm/hour | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHE.06/) |
| 30-minutes | Late Run | 1 Jul 2020 - now | mm/hour | [https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHL.06/](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHHL.06/) |

#### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays hourly, daily and monthly precipitation data  |
| Variable  | Total precipitation  |
| Geographic coverage  | Global 60N-60S, 180W-180E |
| Spatial resolution  | 0.1 degree ~ 11.1 km at equator  |
| Temporal resolution  | 30 minutes, daily and monthly |
| Format  | NetCDF  |
| Unit  | Total mm for given time step, mm/hour, mm/day, and mm/month.  |
| Reference  | https://pmm.gsfc.nasa.gov/GPM  |

#### Downloads

IMERG daily data available at JNB Server Public Directory: J:\Data\GLOBAL\CLIMATE\IMERG


## Climate Indices

A climate index is here defined as a calculated value that can be used to describe the state and the changes in the climate system. Climate indices allow a statistical study of variations of the dependent climatological aspects, such as analysis and comparison of time series, means, extremes and trends.

The following climate indexes are for the precipitation and temperature amount:

### Standardized Precipitation-Evapotranspiration Index (SPEI)

The [SPEI](https://spei.csic.es) is an extension of the widely used Standardized Precipitation Index ([SPI](https://library.wmo.int/doc_num.php?explnum_id=7768)). The SPEI is designed to take into account both `precipitation` and `potential evapotranspiration` (PET) in determining drought. Thus, unlike the SPI, the SPEI captures the main impact of increased temperatures on water demand.

The SPEI can measure drought severity according to its intensity and duration, and can identify the onset and end of drought episodes. The SPEI allows comparison of drought severity through time and space, since it can be calculated over a wide range of climates, as can the SPI. 

The idea behind the SPEI is to compare the highest possible evapotranspiration (what we call the evaporative demand by the atmosphere) with the current water availability. Thus, precipitation (accumulated over a period of time) in the SPEI stands for the water availability, while ETo stands for the atmospheric water demand. 

Negative SPI values represent rainfall deficit and less than median precipitation, and high potential epotranspiration (Dry), starts when the SPEI value is equal or below -1.0. Whereas positive SPEI values indicate rainfall surplus and greater than median precipitation, and low potential epotranspiration (Wet), starts when the SPEI value is equal or above 1.0, and ends when the value becomes negative.

SPEI derived from TerraClimate data

#### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays SPEI-1, 2, 3, 6, 9, 12, 18, 24, 36, 48, 60 and 72-months  |
| Variable  | SPEI  |
| Geographic coverage  | Global 90N-60S, 180W-180E |
| Spatial resolution  | 4-km at equator  |
| Temporal resolution  | monthly.  |
| Format  | GeoTIFF  |
| Unit  | unitless  |

#### Symbology

The threshold and the symbology for the SPEI can follow below color codes and image.

| Class  | Threshold  | Hex  | RGB  |
|---|---|---|---|
| Exceptionally Dry  | -2.00 and below  | `#760005` ![#760005](https://via.placeholder.com/15/760005/000000?text=+)  | rgb(118, 0, 5)  |
| Extremely Dry  | -2.00 to -1.50  | `#ec0013` ![#ec0013](https://via.placeholder.com/15/ec0013/000000?text=+)  | rgb(236, 0, 19)  |
| Severely Dry  | -1.50 to -1.20  | `#ffa938` ![#ffa938](https://via.placeholder.com/15/ffa938/000000?text=+)  | rgb(255, 169, 56)  |
| Moderately Dry  | -1.20 to -0.70  | `#fdd28a` ![#fdd28a](https://via.placeholder.com/15/fdd28a/000000?text=+)  | rgb(253, 210, 138)  |
| Abnormally Dry  | -0.70 to -0.50  | `#fefe53` ![#fefe53](https://via.placeholder.com/15/fefe53/000000?text=+)  | rgb(254, 254, 83)  |
| Near Normal  | -0.50 to +0.50  | `#cccccc` ![#cccccc](https://via.placeholder.com/15/cccccc/000000?text=+)  | rgb(204, 204, 204)  |
| Abnormally Moist  | +0.50 to +0.70  | `#a2fd6e` ![#a2fd6e](https://via.placeholder.com/15/a2fd6e/000000?text=+)  | rgb(162, 253, 110)  |
| Moderately Moist  | +0.70 to +1.20  | `#00b44a` ![#00b44a](https://via.placeholder.com/15/00b44a/000000?text=+)  | rgb(0, 180, 74)  |
| Very Moist  | +1.20 to +1.50  | `#008180` ![#008180](https://via.placeholder.com/15/008180/000000?text=+)  | rgb(0, 129, 128)  |
| Extremely Moist  | +1.50 to +2.00  | `#2a23eb` ![#2a23eb](https://via.placeholder.com/15/2a23eb/000000?text=+)  | rgb(42, 35, 235)  |
| Exceptionally Moist  | +2.00 and above  | `#a21fec` ![#a21fec](https://via.placeholder.com/15/a21fec/000000?text=+)  | rgb(162, 31, 236)  |


### Consecutive Dry Days (CDD)

The number of consecutive dry days (CDD) is the largest number of consecutive days with daily precipitation amount less than 1 mm (or depending on the rain days criteria of the country), within a certain time. Usually the process counts the number of days in the past 90 days to measure the drought level.

#### How it works

Calculate the number of rain days based on the threshold and calculate the count of the most recent days since a rain day or the most recent consecutive string of days that meet the threshold criteria is summed.

Option for rain day's threshold: 1, 2.5, 5, 10 or 20 milimeters of rainfall per day

```
IF previousCDD == null THEN previousCDD == 0
ELSEIF todayRAIN > 1 AND previousCDD == 0 THEN previousCDD + 1
```

CDD derived from IMERG data

#### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays daily CDD  |
| Variable  | CDD  |
| Geographic coverage  | Indonesia 7N-12S, 94E-142E |
| Spatial resolution  | 0.1 degree ~ 11.1 km at equator  |
| Temporal resolution  | Daily  |
| Format  | GeoTIFF  |
| Unit  | Number of day  |

#### Symbology

The threshold and the symbology for the CDD can follow below color codes and image.

| Class  | Threshold  | Hex  | RGB  |
|---|---|---|---|
| No Drought  | 0  | `#cccccc` ![#cccccc](https://via.placeholder.com/15/cccccc/000000?text=+)  | rgb(204, 204, 204)  |
| Very Short  | 1 - 5  | `#ffe5d9` ![#ffe5d9](https://via.placeholder.com/15/ffe5d9/000000?text=+)  | rgb(255, 229, 217)  |
| Short  | 6 - 10  | `#fcbba2` ![#fcbba2](https://via.placeholder.com/15/fcbba2/000000?text=+)  | rgb(252, 187, 162)  |
| Moderate  | 11 - 20  | `#fc9272` ![#fc9272](https://via.placeholder.com/15/fc9272/000000?text=+)  | rgb(252, 146, 114)  |
| Long  | 21 - 30  | `#fa6948` ![#fa6948](https://via.placeholder.com/15/fa6948/000000?text=+)  | rgb(250, 105, 72)  |
| Very Long  | 31 - 60  | `#de2c26` ![#de2c26](https://via.placeholder.com/15/de2c26/000000?text=+)  | rgb(222, 44, 38)  |
| Extreme Drought  | +60  | `#a60f14` ![#a60f14](https://via.placeholder.com/15/a60f14/000000?text=+)  | rgb(166, 15, 20)  |


# How-to guides

You will find step-by-step guideline to calculate climate indices, and can try different (data source and format) approach below.

1. [SPEI using TerraClimate data](https://github.com/bennyistanto/climate-data-application/blob/main/SPEI_using_TerraClimate_data.md)
2. Drought analysis using SPEI
3. CDD using IMERG data
4. Drought analysis using CDD