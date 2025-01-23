import geopandas as gpd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data
gdf = gpd.read_file('cleaned_data1.shp').to_crs(epsg=4326)

# Prepare data
X = gdf[['AADT_mean_']]  # Independent variable
y = gdf['NumStation']  # Dependent variable
X = sm.add_constant(X)  # Add constant term

# Build regression model
model = sm.OLS(y, X).fit()

# Add regression results to GeoDataFrame
gdf['predicted_numstation'] = model.predict(X)
gdf['residuals'] = gdf['NumStation'] - gdf['predicted_numstation']

# Visualization
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Color display for predicted number of stations
gdf.plot(column='predicted_numstation', ax=ax, legend=True,
         legend_kwds={'label': "Predicted Number of Stations"},
         cmap='viridis')

# Highlight high-residual areas, i.e., areas with high AADT but low number of stations
gdf[gdf['residuals'] > 0].plot(ax=ax, color='red', markersize=10)

plt.title('Predicted Number of Stations and High-Residual Areas')
plt.show()