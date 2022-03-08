# Consecutive Wet Days

The number of consecutive wet days (CWD) is similar to the above CDD, the largest number of consecutive days with daily precipitation amount more than 1 mm (or depend on the rain days criteria of the country), within a certain time. Usually the process counts the number of days in the past 90 days to measure the wet level.

## How it works

Calculate the number of rain days based on the threshold and calculate the count of the most recent days since a dry day or the most recent consecutive string of days that meet the threshold criteria is summed.

Option for rain day's threshold: 1, 2.5, 5, 10 or 20 milimeters of rainfall per day

```
IF previousCWD == null THEN previousCWD == 0
ELSEIF todayRAIN < 1 AND previousCWD == 0 THEN previousCWD + 1
```

CWD derived from IMERG data

### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Display daily CWD  |
| Variable  | CWD  |
| Geographic coverage  | Global 60N-60S, 180W-180E |
| Spatial resolution  | 0.1 degree ~ 11.1 km at equator  |
| Temporal resolution  | Daily  |
| Format  | GeoTIFF  |
| Unit  | Number of day  |

### Symbology

The threshold and the symbology for the CWD can follow below color codes and image.

| Class  | Threshold  | Hex  | RGB  |
|---|---|---|---|
| No Rainfall  | 0  | `#cccccc` ![#cccccc](https://via.placeholder.com/15/cccccc/000000?text=+)  | rgb(204, 204, 204)  |
| Very Short  | 1 - 5  | `#ffffcc` ![#ffffcc](https://via.placeholder.com/15/ffffcc/000000?text=+)  | rgb(255, 255, 204)  |
| Short  | 6 - 10  | `#c6e8b3` ![#c6e8b3](https://via.placeholder.com/15/c6e8b3/000000?text=+)  | rgb(198, 232, 179)  |
| Moderate  | 11 - 20  | `#7eccba` ![#7eccba](https://via.placeholder.com/15/7eccba/000000?text=+)  | rgb(126, 204, 186)  |
| Long  | 21 - 30  | `#41b7c4` ![#41b7c4](https://via.placeholder.com/15/41b7c4/000000?text=+)  | rgb(65, 183, 196)  |
| Very Long  | 31 - 60  | `#2c80b8` ![#2c80b8](https://via.placeholder.com/15/2c80b8/000000?text=+)  | rgb(44, 128, 184)  |
| Extreme Wet  | +60  | `#253494` ![#253494](https://via.placeholder.com/15/253494/000000?text=+)  | rgb(37, 52, 148)  |

## Data access

Global CWD data available at DEC S3: `s3://wbgdecinternal-ntl/climate/products/cwd-imerg`