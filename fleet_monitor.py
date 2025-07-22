# Fleet monitor in real time
# Practice functions, loops, and data processing

def calculate_vehicle_status(vehicle_id, speed, fuel_level, last_maintenance_km, current_km):
    """Calculate comprehensice vehicle status."""
    if speed <= 30:
        speed_category = "City"
    if speed <= 60:
        speed_category = "Suburban"
    if speed <= 120:
        speed_category = "Highway"
    else:
        speed_category = "High speed"
    
    # fuel block
    if fuel_level < 20:
        fuel_status = "Critical"
    if fuel_level < 50:
        fuel_status = "Low"
    else:
        fuel_status = "OK"

    # maintenance block
    km_since_last_maintenance = current_km - last_maintenance_km
    if km_since_last_maintenance > 10000:
        maintenance_status = "Due"
    elif km_since_last_maintenance > 8000:
        maintenance_status = "Due soon"
    else:
        maintenance_status = "OK"

    return{
        'vehicle_id': vehicle_id,
        'speed': speed,
        'fuel_level': fuel_level,
        'fuel_status': fuel_status,
        'maintenance_status': maintenance_status,
        'km_since_last_maintenance': km_since_last_maintenance,
        
    }

def print_fleet_summary(fleet_data):
    """Print a summary of the fleet data."""
    total_vehicles = len(fleet_data)
    speeds = [vehicle['speed'] for vehicle in fleet_data]
    fuel_levels = [vehicle['fuel_level'] for vehicle in fleet_data]

    print(f"\n Fleet Summary:")
    print(f"Total Vehicles: {total_vehicles}")
    print(f"average Speed: {sum(speeds)/total_vehicles:.1f} km/h")
    print(f"Average Fuel Level: {sum(fuel_levels)/total_vehicles:.1f} %")
    print(f"Max speed: {max(speeds)} km/h")
    print(f"Min fuel level: {min(fuel_levels)} %")

# Fleet data (vehicle_id, speed, fuel_level, last_maintenance_km, current_km)
fleet_data= [ 
                    [ 'V123', 45, 30, 50000, 60000 ],
                    [ 'BV456', 75, 15, 45000, 55000 ],
                    ['CV789', 90, 50, 30000, 40000],
                      ['DV012', 120, 10, 20000, 30000],
                      ['EV345', 60, 40, 10000, 20000],
                      ['FV678', 30, 25, 60000, 70000]
    

    ]

# Process each vhicle 
fleet_status = []
for vehicle_data in fleet_data:
    vehicle_id, speed, fuel_level, last_maintenance_km, current_km = vehicle_data
    status = calculate_vehicle_status(vehicle_id, speed, fuel_level, last_maintenance_km, current_km)
    fleet_status.append(status)

# Fleet monitor in real time for each vehicle
print('\n Individual Vehicle Status:')
print('-'* 40)
for vehicle in fleet_status:
    print(f"Vehicle ID: {vehicle['vehicle_id']}")
    print(f"Speed: {vehicle['speed']} km/h")
    print(f"Fuel Level: {vehicle['fuel_level']}% ({vehicle['fuel_status']})")
    print(f"Maintenance Status: {vehicle['maintenance_status']} (km since last maintenance: {vehicle['km_since_last_maintenance']})")
    print('-' * 40)


# Alerts and notifications
print('ALERTS:')
for vehicle in fleet_status:
    if vehicle['fuel_status'] == 'Critical':
        print(f"Alert: Vehicle {vehicle['vehicle_id']} has critical fuel level!")
    elif vehicle['maintenance_status'] == 'Due':
        print(f"Alert: Vehicle {vehicle['vehicle_id']} is due for maintenance!")

print_fleet_summary(fleet_status)