import geopandas as gpd
from shapely.geometry import Point
import numpy as np

# Define the center of Johor Baharu, Malaysia
johor_baharu_center = Point(102.7414, 1.8854)  # Longitude, Latitude

# Generate a grid of points around Johor Baharu
num_points = 500  # Number of points to generate
min_distance = 0.1  # Minimum distance from the center in degrees (approximately 11 km)
max_distance = 1.0  # Maximum distance from the center in degrees (approximately 111 km)

# Create an array to hold the points
points = []

# Generate points with a higher density near the center and fewer points further away
while len(points) < num_points:
    lon = np.random.uniform(johor_baharu_center.x, johor_baharu_center.x + max_distance)
    lat = np.random.uniform(johor_baharu_center.y, johor_baharu_center.y + max_distance)
    
    # Calculate distance from the center
    distance_from_center = np.sqrt((lon - johor_baharu_center.x)**2 + (lat - johor_baharu_center.y)**2)
    
    # Probability of keeping the point decreases linearly with distance
    if np.random.rand() < (1 - distance_from_center / max_distance):
        points.append(Point(lon, lat))

# Create a GeoDataFrame for the points
crs = 'EPSG:4326'  # WGS84 coordinate system
gdf_points = gpd.GeoDataFrame(geometry=points, crs=crs)

# Optionally, you can set the Coordinate Reference System (CRS) of the GeoDataFrame
# gdf_points.crs = crs

# Print GeoDataFrame to see the structure
print(gdf_points.head())



# Optionally, you can set the crs (Coordinate Reference System) of the GeoDataFrame
# gdf.crs = 'EPSG:4326'  # WGS84 coordinate system, if not already set

# Print GeoDataFrame to see the structure
# Define the output GeoPackage file path
output_gpkg = 'example.gpkg'

# Export GeoDataFrame to GeoPackage
gdf_points.to_file(output_gpkg, driver='GPKG')

