# MODIS

[MODIS](https://modis.gsfc.nasa.gov/about/) (or Moderate Resolution Imaging Spectroradiometer) is a key instrument aboard the [Terra](http://terra.nasa.gov/) (originally known as EOS AM-1) and [Aqua](http://aqua.nasa.gov/) (originally known as EOS PM-1) satellites. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere.

There are so many MODIS products, complete list ara available here [https://modis.gsfc.nasa.gov/data/dataprod/](https://modis.gsfc.nasa.gov/data/dataprod/)

## MOD11A1

The MOD11A1 V6 product provides daily land surface temperature (LST) and emissivity values in a 1200 x 1200 kilometer grid. The temperature value is derived from the MOD11_L2 swath product. Above 30 degrees latitude, some pixels may have multiple observations where the criteria for clear-sky are met. When this occurs, the pixel value is the average of all qualifying observations. Provided along with both the day-time and night-time surface temperature bands and their quality indicator layers are MODIS bands 31 and 32 and six observation layers. 

### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Displays daily day and nighttime LST  |
| Variable  | Listed below  |
| Geographic coverage  | Global 90N-90S, 180W-180E |
| Spatial resolution  | 1-km at equator  |
| Temporal resolution  | daily  |
| Original format  | HDF-EOS  |
| Unit  | See list below  |

### List datasets

We are utilising Google Earth Engine ([GEE](https://earthengine.google.com)) to get [MOD11A1](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD11A1#bands) data, and below are list of MOD11A1 bands that available at GEE.

| Name  | Description  | Units | Scale |
|---|---|---|---|
| `LST_Day_1km`  | Daytime Land Surface Temperature  | `Kelvin` | `0.02` |
| `QC_Day`  | Daytime LST Quality Indicators  |  |  |
| `Day_view_time`  | Local time of day observation  | `Hours` | `0.1` |
| `Day_view_angle`  | View zenith angle of day observation  | `Degrees` |  |
| `LST_Night_1km`  | Nighttime Land Surface Temperature  | `Kelvin` | `0.02` |
| `QC_Night`  | Nighttime LST Quality Indicators  |  |  |
| `Night_view_time`  | Local time of night observation  | `Hours` | `0.1` |
| `Night_view_angle`  | View zenith angle of night observation  | `Degrees` |  |
| `Emis_31`  | Band 31 emissivity  |  | `0.002` |
| `Emis_32`  | Band 32 emissivity  |  | `0.002` |
| `Clear_day_cov`  | Day clear-sky coverage  |  | `0.0005` |
| `Clear_night_cov`  | Night clear-sky coverage  |  | `0.0005` |

We wrote a GEE [code](https://code.earthengine.google.com/c8733dbad095ad6e5b259142e9d882e7) to get some variables that required by the team for different purposes. Currently we have data covering Indonesia and Latin America Countries, and the variables are listed below:

| Variables  | Units |
|---|---|
| Annual 24h mean LST  | `degC` |
| Annual daytime mean LST  | `degC` |
| Number of annual hotdays based on 24h mean daily LST  | `days` |
| Number of annual hotdays based on daytime daily LST  | `days` |

### Symbology

The threshold and the symbology for the `daily` land surface temperature in degree celcius (°C) can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| -40 and below  | `#b2182b` ![#b2182b](https://via.placeholder.com/15/b2182b/000000?text=+) | rgb(178, 24, 43)  |
| -40 to -30  | `#d6604d` ![#d6604d](https://via.placeholder.com/15/d6604d/000000?text=+)  | rgb(214, 96, 77)  |
| -30 to -20  | `#f4a582` ![#f4a582](https://via.placeholder.com/15/f4a582/000000?text=+)  | rgb(244, 165, 130)  |
| -20 to -10  | `#fddbc7` ![#fddbc7](https://via.placeholder.com/15/fddbc7/000000?text=+)  | rgb(253, 219, 199)  |
| -10 to +10  | `#f7f7f7` ![#f7f7f7](https://via.placeholder.com/15/f7f7f7/000000?text=+)  | rgb(247, 247, 247)  |
| +10 to +20  | `#d1e5f0` ![#d1e5f0](https://via.placeholder.com/15/d1e5f0/000000?text=+)  | rgb(209, 229, 240)  |
| +20 to +30  | `#92c5de` ![#92c5de](https://via.placeholder.com/15/92c5de/000000?text=+)  | rgb(146, 197, 222)  |
| +30 to +40  | `#4393c3` ![#4393c3](https://via.placeholder.com/15/4393c3/000000?text=+)  | rgb(67, 147, 195)  |
| +40 and above  | `#2166ac` ![#2166ac](https://via.placeholder.com/15/2166ac/000000?text=+)  | rgb(33, 102, 172)  |

### Data access

Annual temperature and hotdays also available at DEC S3: `s3://wbgdecinternal-ntl/climate/data/modis/mod11a1/annual`