# Rainfall anomaly

The objective of rainfall anomaly is to evaluate the quality of monthly rainfall over the country. This is achieved through analysis of anomalies, i.e. a comparison against a reference. The classic reference is the long-term average. 

Rainfall anomaly is generated based on dekad data. The model will calculate the accumulated rainfall and other climate indices of precipitation based on that data during the most recent dekad which has been aggregated from pentad estimates. Every month has three dekads, such that the first two dekads have 10 days (i.e., 1-10, 11-20), and the third is comprised of the remaining days of the month (21-28 or 21-29 or 21-30 or 21-31. Therefore, the length of the third dekad of each month is not consistent and varies from 8-11 days, depending on the length of the month.

**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | Displays dekad and monthly rainfall anomaly data  |
| Variable  | Rainfall anomaly  |
| Geographic coverage  | Global 50N-50S, 180W-180E |
| Spatial resolution  | 0.05 degree ~ 5.6 km at equator  |
| Temporal resolution  | dekad, 1-month, 3-month, 6-month, 9-month and 12-month, rolling by dekad.  |
| Format  | GeoTIFF  |
| Unit  | Percent (%) and milimeters  |

## Ratio anomaly

The anomaly is calculated based on percentage of the average

`Anomaly (%) = 100 * rainfall/mean_rainfall`

where `rainfall` is current rainfall and `mean_rainfall` is long-term average of rainfall.

Rainfall anomaly derived from CHIRPS data

**Symbology**

The threshold and the symbology for the ratio anomaly can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| 40% and below  | `#a16622` ![#a16622](https://via.placeholder.com/15/a16622/000000?text=+) | rgb(161, 102, 34)  |
| 40 to 60%  | `#db9835` ![#db9835](https://via.placeholder.com/15/db9835/000000?text=+)  | rgb(219, 152, 53)  |
| 60 to 80%  | `#eec883` ![#eec883](https://via.placeholder.com/15/eec883/000000?text=+)  | rgb(238, 200, 131)  |
| 80 to 90%  | `#fcebb6` ![#fcebb6](https://via.placeholder.com/15/fcebb6/000000?text=+)  | rgb(252, 235, 182)  |
| 90 to 110%  | `#ffffff` ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)  | rgb(255, 255, 255)  |
| 110 to 120%  | `#caf8f9` ![#caf8f9](https://via.placeholder.com/15/caf8f9/000000?text=+)  | rgb(202, 248, 249)  |
| 120 to 140%  | `#91e0ee` ![#91e0ee](https://via.placeholder.com/15/91e0ee/000000?text=+)  | rgb(145, 224, 238)  |
| 140 to 180%  | `#50b7da` ![#50b7da](https://via.placeholder.com/15/50b7da/000000?text=+)  | rgb(80, 183, 218)  |
| 180% and above  | `#3d78cf` ![#3d78cf](https://via.placeholder.com/15/3d78cf/000000?text=+)  | rgb(61, 120, 207)  |


## Data access

!!! info "**Location**"

    **Sharepoint:**
    
    - Ratio anomaly, Dekad [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EtfaLKKACf1LipG27L0mRF0BEvarS4Bn8sRTxU0LIpS5Jw?e=Ak09im](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EtfaLKKACf1LipG27L0mRF0BEvarS4Bn8sRTxU0LIpS5Jw?e=Ak09im)<br>
    - Ratio anomaly, 1-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EqotOvFmGa5HoqJFC5lq3fUBYFPINRhlDM7lQE5BM53Jag?e=SJXEii](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EqotOvFmGa5HoqJFC5lq3fUBYFPINRhlDM7lQE5BM53Jag?e=SJXEii)<br>
    - Ratio anomaly, 3-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EkejiQYYiatJjejkb80WvygBDpyLrofsp2he4W2ebCcZYw?e=kpaQcd](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EkejiQYYiatJjejkb80WvygBDpyLrofsp2he4W2ebCcZYw?e=kpaQcd)<br>
    - Ratio anomaly, 6-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EpLJMPu1OSlLkFiQbkUnG7YBYxIRdbI_Kutf3Rk0lTBEyA?e=qdgXYa](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EpLJMPu1OSlLkFiQbkUnG7YBYxIRdbI_Kutf3Rk0lTBEyA?e=qdgXYa)<br>
    - Ratio anomaly, 9-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EqAjouiGkVpHg5u_xEet70gBfazjZXOa1p8gV_QEahyIOw?e=J0uPbc](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EqAjouiGkVpHg5u_xEet70gBfazjZXOa1p8gV_QEahyIOw?e=J0uPbc)<br>
    - Ratio anomaly, 12-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/Ert1L3SbGFVCuVE3uuU5XNUBkC1FRSvYM3B1ZVyYlDTd1g?e=rkO2h3](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/Ert1L3SbGFVCuVE3uuU5XNUBkC1FRSvYM3B1ZVyYlDTd1g?e=rkO2h3)<br>
    - Ratio anomaly, 24-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/Etylxw8leGVHvC-OQGr7nQgBwl81-gNIQShZSeMLfKZtlQ?e=nYh6Be](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/Etylxw8leGVHvC-OQGr7nQgBwl81-gNIQShZSeMLfKZtlQ?e=nYh6Be)


## Difference anomaly

The anomaly is calculated based on difference of the average

`Anomaly (mm) = rainfall - mean_rainfall`

where `rainfall` is current rainfall and `mean_rainfall` is long-term average of rainfall.

Difference anomaly derived from CHIRPS data

## Data access

!!! info "**Location**"

    **Sharepoint:**
    
    - Difference anomaly, 1-month [https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EssqJNouCZhGpC2acGi-feQB5xLW7LfM1tx-pmR27Pph0g?e=tZjuLb](https://wfp.sharepoint.com/:f:/s/RBBGISEO-3/EssqJNouCZhGpC2acGi-feQB5xLW7LfM1tx-pmR27Pph0g?e=tZjuLb)