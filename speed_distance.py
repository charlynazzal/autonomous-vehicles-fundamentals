# Speed and distance of vehicle

print("Speed and Distance Calculator")

# Get current vehicle state

current_speed = float(input("Enter current speed (km/hr): "))
distance_to_destination = float(input("Enter distance to destination (km): "))
speed_limit = int(input("Speed limit on the road (km/hr): "))

# Time calculations
time_at_current_speed = distance_to_destination / current_speed
time_at_speed_limit = distance_to_destination / speed_limit

print(f"\nResults")
print(f"At current speed ({current_speed} km/hr): {time_at_current_speed:.2f} hours")
print(f"At speed limit: ({speed_limit} km/hr): {time_at_speed_limit:.3f} hours")
print(f"Time difference: {abs(time_at_speed_limit - time_at_current_speed):.3f} hours")

# Speed check
if current_speed > speed_limit:
    excess_speed = current_speed - speed_limit
    print(f"You are {excess_speed} above the speed limit")
elif current_speed == speed_limit:
    print ("Heads up, you are at the speed limit")
else:
    print("Speed within limit")
