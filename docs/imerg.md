# IMERG

The GPM is next-generation of the Tropical Rainfall Measuring Mission (TRMM - https://pmm.nasa.gov/TRMM). Like the TRMM, the GPM mission aims at providing uniformly calibrated precipitation estimates at a quasi-global scale by merging the measurements from its constellation of microwave and IR satellites. All GPM data sets including measurements obtained from each platform (Level 2) are available on the PMM site (https://pmm.nasa.gov/data-access). Among many GPM products, the Multi-satellitE Retrievals for GPM (IMERG) is most interesting to the users since it delivers the ‘best’ precipitation estimates by combining data obtained from all available microwave and infrared (IR) platforms of the GPM satellite constellation. 

IMERG is adjusted to GPCP monthly climatology zonally to achieve a bias profile that is considered reasonable. Multiple runs for different user requirements for latency and accuracy

1. “Early” – 4 hour (example application: flash flooding)
2. “Late” – 14 hour (crop forecasting)
3. “Final” – 3 months (research)

## List datasets

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

## About the data

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

## Data access

IMERG daily data available at DEC S3: `s3://wbgdecinternal-ntl/climate/data/imerg`