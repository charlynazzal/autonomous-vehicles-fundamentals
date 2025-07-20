# Converting GPS coordinates to landmarks
# Practicing for math operations and string formation

print("GPS converter: ")

# Dubai coordinates
dubai_mall_lat = 25.1972 # Latitude is North and South
dubai_mall_lon = 55.2796 # Longitude is East and West

# Convert to degrees, minutes, seconds format
def decimals_to_degrees(decimals_degrees):
    degrees = int(decimals_degrees)
    minutes_float = float(decimals_degrees-degrees) * 60
    minutes = int(minutes_float)
    seconds = float(minutes_float - minutes)
    return degrees, minutes, seconds

# Convert latitude
lat_deg, lat_min, lat_sec = decimals_to_degrees(abs(dubai_mall_lat))
lat_direction = 'N' if dubai_mall_lat >= 0 else 'S' # Checks if latitude is positive/North or negative/South

# Convert longitude
lon_deg, lon_min, lon_sec = decimals_to_degrees(abs(dubai_mall_lon))
lon_direction = 'E' if dubai_mall_lon >= 0 else 'W' # Checks if longitude is positive/East or negative/West

print(f"Dubai Mall Coordinates: ")
print(f"Decimal: {dubai_mall_lat:.6f}°, {dubai_mall_lon:.6f}°")
print(f"DMS: {lat_deg}°{lat_min}'{lat_sec:.2f}\"{lat_direction}, {lon_deg}°{lon_min}'{lon_sec:.2f}\"{lon_direction}")

# Calculate distance from origin
distance_from_origin = (dubai_mall_lat**2 + dubai_mall_lon**2)**0.5
print(f"Distance from the origin: {distance_from_origin:.6f} units")

