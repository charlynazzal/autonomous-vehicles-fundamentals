# Practice math operations, print statements, vehicle logic

print('Vehicle Parameter Calculator')


vehicle_mass = 1500 # kg
engine_power = 150 # kW
current_fuel = 45  # liters
fuel_capacity = 60 # liters

# Calculate derived parameters
power_to_weight = engine_power / vehicle_mass
fuel_percentage = (current_fuel / fuel_capacity) * 100
remaining_range = (current_fuel * 12) # Assume 12km / liter

print(f"Vehicle Mass: {vehicle_mass} kg")
print(f"Engine Power: {engine_power} kW")
print(f"Power-to-Weight Ratio: {power_to_weight:.2f}")
print(f"Fuel Levels: {fuel_percentage:.1f}%")
print(f"Estimated Range: {remaining_range:.0f} km")

# Safety Checks
if fuel_percentage < 20:
    print("WARNING: Low fuel")
elif fuel_percentage < 50:
    print('Fuel levels below 50%')
else:
    print('Fuel levels are good to go')

# Vehicle Mass (kg): Total weight of the vehicle, important for calculating forces and acceleration

# Engine Power (kW): The power output of the engine (1 kW ≈ 1.34 horsepower)

# Power-to-Weight Ratio: Engine power divided by vehicle mass - key for performance

# Fuel Capacity/Current Fuel: Fuel system parameters (in liters)

# Estimated Range: How far the vehicle can travel with current fuel (km)

# The vehicle's mass affects braking distance and acceleration

# Power-to-weight ratio impacts merging and passing capabilities

# Fuel/energy status determines operational range

# Range estimation is crucial for route planning
