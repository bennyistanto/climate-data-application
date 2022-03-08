# CHIRPS

Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) from Climate Hazard Center (CHC), Department of Geography, University of California Santa Barbara - [https://www.chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps) is a 35+ year quasi-global rainfall data set. Spanning 50°S-50°N (and all longitudes) and ranging from 1981 to near-present, CHIRPS incorporates CHC's in-house climatology, CHPclim, 0.05° resolution satellite imagery, and in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring. 

**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | Displays dekad and monthly rainfall data  |
| Variable  | Total rainfall  |
| Geographic coverage  | Global 50N-50S, 180W-180E |
| Spatial resolution  | 0.05 degree ~ 5.6 km at equator  |
| Temporal resolution  | daily, pentad, dekad, monthly, 2-monthly, 3-monthly and annual  |
| Format  | GeoTIFF, BIL and NetCDF  |
| Unit  | Total mm for given time step, mm/pentad, mm/month, etc.  |
| Source  | [https://data.chc.ucsb.edu/products/CHIRPS-2.0/](https://data.chc.ucsb.edu/products/CHIRPS-2.0/)  |
| Reference  | [https://wiki.chc.ucsb.edu/CHIRPS_FAQ](https://wiki.chc.ucsb.edu/CHIRPS_FAQ)  |

**Symbology**

The threshold and the symbology for the `dekad` rainfall in milimeters can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| No Rain  | `#e1e1e1` ![#e1e1e1](https://via.placeholder.com/15/e1e1e1/000000?text=+) | rgb(225, 225, 225)  |
| 1 to 3  | `#ffffff` ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)  | rgb(255, 255, 255)  |
| 3 to 10  | `#f9f3d5` ![#f9f3d5](https://via.placeholder.com/15/f9f3d5/000000?text=+)  | rgb(249, 243, 213)  |
| 10 to 20  | `#dce2a8` ![#dce2a8](https://via.placeholder.com/15/dce2a8/000000?text=+)  | rgb(220, 226, 168)  |
| 20 to 30  | `#a8c58d` ![#a8c58d](https://via.placeholder.com/15/a8c58d/000000?text=+)  | rgb(168, 197, 141)  |
| 30 to 40  | `#77a87d` ![#77a87d](https://via.placeholder.com/15/77a87d/000000?text=+)  | rgb(119, 168, 125)  |
| 40 to 60  | `#ace8f8` ![#ace8f8](https://via.placeholder.com/15/ace8f8/000000?text=+)  | rgb(172, 232, 248)  |
| 60 to 80  | `#4cafd9` ![#4cafd9](https://via.placeholder.com/15/4cafd9/000000?text=+)  | rgb(76, 175, 217)  |
| 80 to 100  | `#1d5ede` ![#1d5ede](https://via.placeholder.com/15/1d5ede/000000?text=+)  | rgb(29, 94, 222)  |
| 100 to 120  | `#001bc0` ![#001bc0](https://via.placeholder.com/15/001bc0/000000?text=+)  | rgb(0, 27, 192)  |
| 120 to 150  | `#9131f1` ![#9131f1](https://via.placeholder.com/15/9131f1/000000?text=+)  | rgb(145, 49, 241)  |
| 150 to 200  | `#e983f3` ![#e983f3](https://via.placeholder.com/15/e983f3/000000?text=+)  | rgb(233, 131, 243)  |
| +200 and above  | `#f6c7ec` ![#f6c7ec](https://via.placeholder.com/15/f6c7ec/000000?text=+)  | rgb(246, 199, 236)  |

The threshold and the symbology for the `monthly` rainfall in milimeters can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| No Rain  | `#e1e1e1` ![#e1e1e1](https://via.placeholder.com/15/e1e1e1/000000?text=+) | rgb(225, 225, 225)  |
| 1 to 20  | `#ffffff` ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)  | rgb(255, 255, 255)  |
| 20 to 40  | `#f9f3d5` ![#f9f3d5](https://via.placeholder.com/15/f9f3d5/000000?text=+)  | rgb(249, 243, 213)  |
| 40 to 60  | `#dce2a8` ![#dce2a8](https://via.placeholder.com/15/dce2a8/000000?text=+)  | rgb(220, 226, 168)  |
| 60 to 80  | `#a8c58d` ![#a8c58d](https://via.placeholder.com/15/a8c58d/000000?text=+)  | rgb(168, 197, 141)  |
| 80 to 100  | `#77a87d` ![#77a87d](https://via.placeholder.com/15/77a87d/000000?text=+)  | rgb(119, 168, 125)  |
| 100 to 125  | `#ace8f8` ![#ace8f8](https://via.placeholder.com/15/ace8f8/000000?text=+)  | rgb(172, 232, 248)  |
| 125 to 150  | `#4cafd9` ![#4cafd9](https://via.placeholder.com/15/4cafd9/000000?text=+)  | rgb(76, 175, 217)  |
| 150 to 200  | `#1d5ede` ![#1d5ede](https://via.placeholder.com/15/1d5ede/000000?text=+)  | rgb(29, 94, 222)  |
| 200 to 250  | `#001bc0` ![#001bc0](https://via.placeholder.com/15/001bc0/000000?text=+)  | rgb(0, 27, 192)  |
| 250 to 300  | `#9131f1` ![#9131f1](https://via.placeholder.com/15/9131f1/000000?text=+)  | rgb(145, 49, 241)  |
| 300 to 350  | `#e983f3` ![#e983f3](https://via.placeholder.com/15/e983f3/000000?text=+)  | rgb(233, 131, 243)  |
| +350 and above  | `#f6c7ec` ![#f6c7ec](https://via.placeholder.com/15/f6c7ec/000000?text=+)  | rgb(246, 199, 236)  |

**Downloads**

!!! info "**Location**"

    Sharepoint: [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EmDYs8Wl_tlEqDNVBIhMMEEB6s-LNcoD4ET1GYPmJ_xjKQ?e=ikAANf](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EmDYs8Wl_tlEqDNVBIhMMEEB6s-LNcoD4ET1GYPmJ_xjKQ?e=ikAANf)

    For latest data, please check their official website.
