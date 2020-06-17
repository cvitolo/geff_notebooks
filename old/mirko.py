import salem
shapefile = "/Users/mirkodandrea/.salem_cache/salem-sample-data-b6d201fd8c228d5a1a6ea97964ef769dfef186ec/shapes/world_borders/world_borders.shp"
ds_name = "ECMWF_FWI_20180710_1200_hr_fwi.nc"
ds = xr.open_dataset(ds_name)
ds


# Load the shapefile
shp_df = salem.read_shapefile(shapefile)
shp_df.head(5)

# Query for the US
shp_df_us = shdf.query('CNTRY_NAME=="United States"')
shp_df_us.head()

# mask the dataset on the selected geometries
ds_us = ds.salem.roi(shape=shp_df_us)

# Plot the mean value over time 
plt.imshow(ds_us.fwi.mean('time'))
