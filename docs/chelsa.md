# CHELSA

[CHELSA](https://chelsa-climate.org) (Climatologies at high resolution for the earth’s land surface areas) is a very high resolution (`30 arcsec`, `~1km`) global downscaled climate data set currently hosted by the Swiss Federal Institute for Forest, Snow and Landscape Research WSL. It is built to provide free access to high resolution climate data for research and application, and is constantly updated and refined.

## About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays daily climate datasets  |
| Variable  | Listed below  |
| Geographic coverage  | Global 90N-90S, 180W-180E |
| Spatial resolution  | 1-km at equator  |
| Temporal resolution  | daily  |
| Format  | netCDF  |
| Unit  | See list below  |

## List datasets

CHELSA provides `daily timeseries`, `monthly timeseries`,  `Bioclimate/Köppen-Geiger`, `Future` and `Paleo Climate` data. To support current project, GOST utilise daily timeseries temperature data from CHELSA-W5E5.

### CHELSA-W5E5 v1.0

[CHELSA-W5E5](https://chelsa-climate.org/chelsa-w5e5-v1-0-daily-climate-data-at-1km-resolution/) dataset covers the entire globe at `30 arcsec` horizontal and daily temporal resolution from 1979 to 2016. Variables (with short names and units in brackets) included in the CHELSA-W5E5 dataset are:

| Name  | Description  | Units |
|---|---|---|
| `pr`  | Daily Mean Precipitation  | `kg m-2 s-1` |
| `rsds`  | Daily Mean Surface Downwelling Shortwave Radiation  | `W m-2` |
| `tas`  | Daily Mean Near-Surface Air Temperature  | `K` |
| `tasmin`  | Daily Minimum Near Surface Air Temperature  | `K` |
| `tasmax`  | Daily Maximum Near Surface Air Temperature  | `K` |
| `orog`  | Surface Altitude  | `m` |
| `mask`  | the CHELSA-W5E5 land-sea mask  | `1` |

## Data access

Individual monthly download link: [https://data.isimip.org/10.48364/ISIMIP.836809](https://data.isimip.org/10.48364/ISIMIP.836809)

Daily min and max temperature also available at DEC S3: `s3://wbgdecinternal-ntl/climate/data/chelsa`
