# Standardized Precipitation-Evapotranspiration Index (SPEI)

The [SPEI](https://spei.csic.es) is an extension of the widely used SPI. The SPEI is designed to take into account both `precipitation` and `potential evapotranspiration` (PET) in determining drought. Thus, unlike the SPI, the SPEI captures the main impact of increased temperatures on water demand.

The SPEI can measure drought severity according to its intensity and duration, and can identify the onset and end of drought episodes. The SPEI allows comparison of drought severity through time and space, since it can be calculated over a wide range of climates, as can the SPI. 

The idea behind the SPEI is to compare the highest possible evapotranspiration (what we call the evaporative demand by the atmosphere) with the current water availability. Thus, precipitation (accumulated over a period of time) in the SPEI stands for the water availability, while ETo stands for the atmospheric water demand. 

Negative SPEI values represent rainfall deficit and less than median precipitation, and high potential epotranspiration (Dry), starts when the SPEI value is equal or below -1.0. Whereas positive SPEI values indicate rainfall surplus and greater than median precipitation, and low potential epotranspiration (Wet), starts when the SPEI value is equal or above 1.0, and ends when the value becomes negative.

SPEI derived from TerraClimate data

## About the data

| Characteristic  | Description  |
|---|---|
| Function  | Display SPEI-1, 2, 3, 6, 9, 12, 18, 24, 36, 48, 60 and 72-months  |
| Variable  | SPEI  |
| Geographic coverage  | Global 90N-60S, 180W-180E |
| Spatial resolution  | 4-km at equator  |
| Temporal resolution  | monthly.  |
| Format  | GeoTIFF  |
| Unit  | unitless  |

## Symbology

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

## Data access

Global SPEI-12 data available at DEC S3: `s3://wbgdecinternal-ntl/climate/products/spei-terraclimate`