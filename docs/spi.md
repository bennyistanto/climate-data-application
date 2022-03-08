# Standardized Precipitation Index

The Standardized Precipitation Index ([SPI](https://library.wmo.int/doc_num.php?explnum_id=7768)) is a normalized index representing the probability of occurrence of an observed rainfall amount when compared with the rainfall climatology over a long-term period. This long-term record is fitted to a probability distribution, which is then transformed into a normal distribution so that the mean SPI for the location and desired period is zero.

Negative SPI values represent rainfall deficit and less than median precipitation (Dry), starts when the SPI value is equal or below -1.0. Whereas positive SPI values indicate rainfall surplus and greater than median precipitation (Wet), starts when the SPI value is equal or above 1.0, and ends when the value becomes negative.

## How it works
- Precipitation is normalized using a probability distribution function so that values of SPI are actually seen as standard deviations from the median.
- A normalized distribution allows for estimation of both dry and wet periods.
- Accumulated values can be used to analyse drought severity (magnitude).
- At least 30 years of continuous monthly precipitation data are needed but longer-term records would be preferable.
- SPI timescale intervals shorter than 1 month and longer than 24 months may be unreliable.
- It is spatially invariant in its interpretation.
- Its probability-based nature (probability of observed precipitation transformed into an index) makes it well suited to risk management and triggers for decision-making.

SPI derived from CHIRPS and TerraClimate data

### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Display SPI-1, 2, 3, 6, 9, 12, 18, 24, 36, 48, 60 and 72-months  |
| Variable  | SPI  |
| Geographic coverage  | Global 50N-50S, 180W-180E (CHIRPS) and Global 90N-90S, 180W-180E (TerraClimate) |
| Spatial resolution  | 0.05 degree ~ 5.6 km at equator (CHIRPS) and 4-km at equator (TerraClimate)  |
| Temporal resolution  | monthly.  |
| Format  | GeoTIFF  |
| Unit  | unitless  |

### Symbology

The threshold and the symbology for the SPI can follow below color codes and image.

| Class  | Threshold  | Hex  | RGB  |
|---|---|---|---|
| Exceptionally Dry  | -2.00 and below  | `#760005` ![#760005](https://via.placeholder.com/15/760005/000000?text=+)  | rgb(118, 0, 5)  |
| Extremely Dry  | -2.00 to -1.50  | `#ec0013` ![#ec0013](https://via.placeholder.com/15/ec0013/000000?text=+)  | rgb(236, 0, 19)  |
| Severely Dry  | -1.50 to -1.20  | `#ffa938` ![#ffa938](https://via.placeholder.com/15/ffa938/000000?text=+)  | rgb(255, 169, 56)  |
| Moderately Dry  | -1.20 to -0.70  | `#fdd28a` ![#fdd28a](https://via.placeholder.com/15/fdd28a/000000?text=+)  | rgb(253, 210, 138)  |
| Abnormally Dry  | -0.70 to -0.50  | `#fefe53` ![#fefe53](https://via.placeholder.com/15/fefe53/000000?text=+)  | rgb(254, 254, 83)  |
| Near Normal  | -0.50 to +0.50  | `#ffffff` ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)  | rgb(255, 255, 255)  |
| Abnormally Moist  | +0.50 to +0.70  | `#a2fd6e` ![#a2fd6e](https://via.placeholder.com/15/a2fd6e/000000?text=+)  | rgb(162, 253, 110)  |
| Moderately Moist  | +0.70 to +1.20  | `#00b44a` ![#00b44a](https://via.placeholder.com/15/00b44a/000000?text=+)  | rgb(0, 180, 74)  |
| Very Moist  | +1.20 to +1.50  | `#008180` ![#008180](https://via.placeholder.com/15/008180/000000?text=+)  | rgb(0, 129, 128)  |
| Extremely Moist  | +1.50 to +2.00  | `#2a23eb` ![#2a23eb](https://via.placeholder.com/15/2a23eb/000000?text=+)  | rgb(42, 35, 235)  |
| Exceptionally Moist  | +2.00 and above  | `#a21fec` ![#a21fec](https://via.placeholder.com/15/a21fec/000000?text=+)  | rgb(162, 31, 236)  |

## Data access

Global SPI data available at DEC S3:

1. CHIRPS: `s3://wbgdecinternal-ntl/climate/products/spi-chirps`
2. TerraClimate: `s3://wbgdecinternal-ntl/climate/products/spi-terraclimate`
