# GOST Climate

This is the climate analytics repository from the **Global Operational Support Team** ([GOST](https://www.worldbank.org/en/research/brief/geospatial-operations-support-team-at-the-world-bank)).

-----

## Contents

This section describes in detail list of data provider, derived products, step-by-step to do the analysis and some example of use case of the data, to meet the user requirements of the GOST team of the World Bank at country, regional and global level. 

Currently, GOST Climate contains:

### Data

The climate are varies by location and by time of year. Daily and monthly rainfall, daily and monthly temperature and potential evapotranspiration are a few of the many datasets from various data providers.

### Climate Indices

A climate index is here defined as a calculated value that can be used to describe the state and the changes in the climate system. Climate indices allow a statistical study of variations of the dependent climatological aspects, such as analysis and comparison of time series, means, extremes and trends.

### How-to guides

You will find step-by-step guideline to calculate climate indices, and can try different (data source and format) approach in How-to? section.

### Case

Example of use case from the WBG project.

-----

## Where to find?

You can access the data via [AWS S3](https://aws.amazon.com/s3/) and soon at Development Data Hub ([DDH](https://datacatalog.worldbank.org/home))

### AWS S3

All the data and derivative product are located at DEC S3 bucket: `s3://wbgdecinternal-ntl/climate` with below structure

??? info "Folder structure"
    ```
    ├── data                            # Data folder
    │   ├── README.txt
    │   ├── chelsa
    │   │   ├── original
    │   │   │   ├── nc-precip
    │   │   │   ├── nc-tmax
    │   │   │   ├── nc-tmean
    │   │   │   ├── nc-tmin
    │   │   │   ├── README.txt
    │   │   ├── global
    │   │   ├── lac    
    │   ├── chirps
    │   │   ├── monthly
    │   │   │   ├── geotiff
    │   │   │   ├── nc
    │   │   │   ├── README.txt
    │   ├── imerg
    │   │   ├── geotiff
    │   │   │   ├── rainfall_1days
    │   │   │   ├── rainfall_1days_annual_max
    │   │   │   ├── rainfall_1days_monthly_max
    │   │   │   ├── rainfall_annual
    │   │   │   ├── rainfall_monthly
    │   │   │   ├── rainfall_monthly_statistics
    │   │   │   ├── README.txt
    │   │   ├── nc
    │   │   │   ├── README.txt
    │   ├── modis
    │   │   ├── mod11a1
    │   │   │   ├── annual
    │   │   │   │   ├── hotdays_from_lst_24h_mean
    │   │   │   │   ├── hotdays_from_lst_day_mean
    │   │   │   │   ├── lst_24h_mean
    │   │   │   │   ├── lst_day_mean
    │   │   │   ├── README.txt
    │   ├── terraclimate
    │   │   ├── aet
    │   │   ├── climatologies
    │   │   ├── def
    │   │   ├── layers
    │   │   ├── pdsi
    │   │   ├── pet
    │   │   ├── plus2c
    │   │   ├── plus4c
    │   │   ├── ppt
    │   │   ├── q
    │   │   ├── soil
    │   │   ├── srad
    │   │   ├── summaries
    │   │   ├── swe
    │   │   ├── tas
    │   │   ├── tmax
    │   │   ├── tmin
    │   │   ├── vap
    │   │   ├── vpd
    │   │   ├── ws
    │   │   ├── README.txt
    ├── products                            # Producst folder
    │   ├── README.txt
    │   ├── cdd-imerg
    │   │   ├── cdd_1mm
    │   │   ├── cdd_5mm
    │   │   ├── README.txt
    │   ├── cwd-imerg
    │   │   ├── cwd_1mm
    │   │   ├── cwd_5mm
    │   │   ├── README.txt
    │   ├── drydays-imerg
    │   │   ├── drydays_1mm
    │   │   ├── drydays_5mm
    │   │   ├── README.txt
    │   ├── spei-terraclimate
    │   │   ├── geotiff
    │   │   │   ├── spei12
    │   │   │   ├── spei12-derivative-product
    │   │   │   │   ├── consecutive_dry_month 
    │   │   │   │   ├── consecutive_dry_month_max
    │   │   │   │   ├── dry_month
    │   │   │   │   ├── dry_month_total
    │   │   ├── nc
    │   │   ├── README.txt
    │   ├── spi-chirps
    │   │   ├── geotiff
    │   │   │   ├── spi01
    │   │   │   ├── spi02
    │   │   │   ├── spi03
    │   │   │   ├── spi06
    │   │   │   ├── spi09
    │   │   │   ├── spi12
    │   │   │   ├── spi24
    │   │   │   ├── spi36
    │   │   │   ├── spi48
    │   │   │   ├── spi60
    │   │   │   ├── spi72
    │   │   ├── nc
    │   │   ├── README.txt
    │   ├── wetdays-imerg
    │   │   ├── wetdays_1mm
    │   │   ├── wetdays_5mm
    │   │   ├── README.txt
    ```

### Development Data Hub

Currently we are still working on it, hope the data available at DDH soon. Stay tune!

-----

## Disclaimer

The data, climate derivative product and code available in this repository may produce results containing geographic information with limitations due to the scale, resolution, date and interpretation of the original source materials. No liability concerning the content or the use thereof is assumed by the producer.


## Help

This documentation is created and maintained by the GOST team. You can help us improve this guide by simply sending your feedback or by contributing directly to it via [Github](http://github.com/worldbank/GOST_Climate).

For further information about this documentation, please contact:

**The Global Operational Support Team**<br>
Data Analytics and Tools, DECDG<br>
The World Bank<br>

<img src="./img/WBG_Horizontal-RGB-web.png" width="150">