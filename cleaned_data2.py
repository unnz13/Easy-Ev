import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Define file paths
input_file_path = '/Users/sangruoxuan/Downloads/NumStation+AADT/cleaned_data.csv'
output_file_path = '/Users/sangruoxuan/Downloads/NumStation+AADT/cleaned_data1.shp'

# Load data
data = pd.read_csv(input_file_path)

# Clean data: Remove rows containing NaN values, ensuring all required fields are filled
data.dropna(subset=['INTPTLAT', 'INTPTLON', 'NumStation', 'AADT_mean_', 'vul_int', 'hic_int'], inplace=True)

# Create a GeoDataFrame using point coordinates (longitude, latitude)
gdf = gpd.GeoDataFrame(
    data,
    geometry=[Point(xy) for xy in zip(data['INTPTLON'], data['INTPTLAT'])],
    crs="EPSG:4326"  # Ensure the correct coordinate system is used
)

# Save the cleaned data as a Shapefile
gdf.to_file(output_file_path, driver='ESRI Shapefile')

print("Data cleaned and saved as Shapefile.")