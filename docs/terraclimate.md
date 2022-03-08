# TerraClimate

[TerraClimate](http://www.climatologylab.org/terraclimate.html) is a dataset of monthly climate and climatic water balance for global terrestrial surfaces from 1958-2020. These data provide important inputs for ecological and hydrological studies at global scales that require high spatial resolution and time-varying data. All data have monthly temporal resolution and a 4-km (1/24th degree) spatial resolution. 

#### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays monthly climate datasets  |
| Variable  | Listed below  |
| Geographic coverage  | Global 90N-90S, 180W-180E |
| Spatial resolution  | 4-km at equator  |
| Temporal resolution  | monthly  |
| Format  | GeoTIFF  |
| Unit  | See list below  |

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

#### Data access

Individual years download link: [http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data/catalog.html](http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data/catalog.html)

Also available at DEC S3: `s3://wbgdecinternal-ntl/climate/data/terraclimate`