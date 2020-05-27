# Global ECMWF Fire Forecasting (GEFF) system - notebooks
> Jupyter notebooks to explore, visualise and post-process fire danger reanalysis and forecast data from the GEFF modelling system.

[![DOI](https://zenodo.org/badge/167970290.svg)](https://zenodo.org/badge/latestdoi/167970290)

The European Centre for Medium-Range Weather Forecasts (ECMWF) produces daily fire danger forecasts and reanalysis products from the Global ECMWF Fire Forecast (GEFF) model. Reanalysis (and soon seasonal forecasts) is available through the Copernicus Climate Data Store (CDS) while the medium-range real-time forecast is available through the EFFIS and GWIS platforms, which give access to timely fire danger information at a pan-European and global scale, respectively. Thirty-eight local and national authorities across Europe are part of the EFFIS network and have been relying on GEFF outputs for the early identification of regions prone to fire events as a result of persistent drought conditions.

GEFF-reanalysis provides historical records of global fire danger conditions from 1980 to the present day and it is made of four types of products: (i) deterministic model outputs (called simply 'reanalysis' on the CDS), (ii) probabilistic model outputs (made of 10 ensemble members), (iii) ensemble mean and (iv) ensemble spread. It is updated as soon as new ERA-5 data becomes available (~2 months behind real-time). 
GEFF-realtime provides real-time high-resolution deterministic (~9 Km) and lower-resolution probabilistic (~18Km) fire danger forecasts up to 15 days ahead using weather forcings from the latest model cycle of the ECMWF’s Integrated Forecasting System (IFS). The real-time dataset is updated every day with a new set of forecasts. Forecast data can be requested to EFFIS using an online form.
These products have been developed as part of the EU-funded Copernicus Emergency Management Services (CEMS) and complement other Copernicus products related to fire, such as the biomass-burning emissions made available by the Copernicus Atmosphere Monitoring Service (CAMS).  The development of the GEFF modelling system was funded through a third-party agreement with the European Commission’s Joint Research Centre (JRC). 

GEFF produces fire danger indices based on the Canadian Fire Weather index as well as the US and Australian fire danger models. GEFF datasets are under the Copernicus license, which provides users with free, full and open access to environmental data.

For more information, please refer to the documentation on the CDS and on the EFFIS website.


**References**

*Journal papers*

  - Vitolo, C., Di Giuseppe, F., Krzeminski, B. and San-Miguel-Ayanz, J., 2019. A 1980–2018 global fire danger re-analysis dataset for the Canadian Fire Weather Indices. Scientific data, 6, p.190032.

  - Vitolo, Claudia, Francesca Di Giuseppe, and Mirko D’Andrea. Caliver: An r package for calibration and verification of forest fire gridded model outputs. PLOS ONE, 13(1):1–18, 01 2018

  - Di Giuseppe, F., Pappenberger, F., Wetterhall, F., Krzeminski, B., Camia, A., Libertá, G. and San Miguel, J., 2016. The potential predictability of fire danger provided by numerical weather prediction. Journal of Applied Meteorology and Climatology, 55(11), pp.2469-2491.

*Newsletter articles*

  - ECMWF forecasts support Portugal wildfire response (Number 153 - Autumn - October 2017) https://www.ecmwf.int/en/newsletter/153/news/ecmwf-forecasts-support-portugal-wildfire-response

  - Devastating wildfires in Chile in January 2017 (Number 151 - Spring - April 2017) https://www.ecmwf.int/en/newsletter/151/news/devastating-wildfires-chile-january-2017

  - Copernicus fire danger forecast goes online (Number 151 - Spring - April 2017) https://www.ecmwf.int/en/newsletter/151/news/copernicus-fire-danger-forecast-goes-online

*Software tools*

  - GEFF model source code (Fortran): https://git.ecmwf.int/projects/CEMSF/repos/geff/browse
  - Vitolo C, Di Giuseppe F, D’Andrea M (2018) Caliver: An R package for CALIbration and VERification of forest fire gridded model outputs. PLOS ONE 13(1): e0189419. https://doi.org/10.1371/journal.pone.0189419
  - Claudia Vitolo, & Francesca Di Giuseppe. (2020, May 27). cvitolo/geff_notebooks: geff_notebooks v0.1 (Version v0.1). Zenodo. http://doi.org/10.5281/zenodo.3859592
