# Land Surface Temperature anomaly

The objective is to evaluate the monthly deviation of temperature over the country based on MOD11 data. This is achieved through analysis of Anomalies, (i.e. a comparison against a reference). 

The anomaly is calculated based on difference of the average.

`LST anomaly (°C) = LST - mean_LST`

where:

- `LST` is the current value of LST<br>
- `mean_LST` is the long-term average value of LST.

LST and LST long-term average derived from MODIS data

## About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays 8-days, 16-days and monthly LST anomaly data  |
| Variable  | LST anomaly  |
| Geographic coverage  | Regional (16-days) and Global (monthly)  |
| Spatial resolution  | 5.6 km and 1 km at equator  |
| Temporal resolution  | Monthly, 16-days, and 8-days.  |
| Format  | GeoTIFF  |
| Unit  | Degrees Celcius (°C)  |

## Symbology

The threshold and the symbology for the `8-days` land surface temperature difference anomaly in degree celcius (°C) can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| -10 and below  | `#b2182b` ![#b2182b](https://via.placeholder.com/15/b2182b/000000?text=+) | rgb(178, 24, 43)  |
| -10 to -5  | `#d6604d` ![#d6604d](https://via.placeholder.com/15/d6604d/000000?text=+)  | rgb(214, 96, 77)  |
| -5 to -2  | `#f4a582` ![#f4a582](https://via.placeholder.com/15/f4a582/000000?text=+)  | rgb(244, 165, 130)  |
| -2 to -1  | `#fddbc7` ![#fddbc7](https://via.placeholder.com/15/fddbc7/000000?text=+)  | rgb(253, 219, 199)  |
| -1 to +1  | `#f7f7f7` ![#f7f7f7](https://via.placeholder.com/15/f7f7f7/000000?text=+)  | rgb(247, 247, 247)  |
| +1 to +2  | `#d1e5f0` ![#d1e5f0](https://via.placeholder.com/15/d1e5f0/000000?text=+)  | rgb(209, 229, 240)  |
| +2 to +5  | `#92c5de` ![#92c5de](https://via.placeholder.com/15/92c5de/000000?text=+)  | rgb(146, 197, 222)  |
| +5 to +10  | `#4393c3` ![#4393c3](https://via.placeholder.com/15/4393c3/000000?text=+)  | rgb(67, 147, 195)  |
| +10 and above  | `#2166ac` ![#2166ac](https://via.placeholder.com/15/2166ac/000000?text=+)  | rgb(33, 102, 172)  |

## Data access

!!! info "**Location**"

    **Dropbox:**
    
    - LST anomaly, Monthly [https://www.dropbox.com/sh/zctcgptbswql6ko/AADpgdtzsQ4hZunUGsRrBv74a?dl=0](https://www.dropbox.com/sh/zctcgptbswql6ko/AADpgdtzsQ4hZunUGsRrBv74a?dl=0)

    - LST anomaly, 16-days: [https://www.dropbox.com/sh/k3f1qcu0kbe3inr/AABA30vBhbLHNzk5iwvnlkgFa?dl=0](https://www.dropbox.com/sh/k3f1qcu0kbe3inr/AABA30vBhbLHNzk5iwvnlkgFa?dl=0)