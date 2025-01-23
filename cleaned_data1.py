import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

data = pd.read_csv('/Users/sangruoxuan/Downloads/NumStation+AADT/NumStation+AADT_new.csv')

# Clean data: Remove rows with missing coordinate information
cleaned_data = data.dropna(subset=['block groups_INTPTLAT', 'block groups_INTPTLON'])

gdf = gpd.GeoDataFrame(
    cleaned_data,
    geometry=[Point(xy) for xy in zip(cleaned_data['block groups_INTPTLON'], cleaned_data['block groups_INTPTLAT'])],
    crs="EPSG:4326"
)

gdf.to_file("cleaned_data.shp")
