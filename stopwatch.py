# Import Library
import datetime

# Identify names constant
min_per_hour = 60
seconds_per_minute = 60
seconds_per_hour = 3600

# Get time for start
input("Press Enter to start.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]


# Get time for stop
input("Press Enter again to stop.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]

# Convert separte times all into seconds
total_seconds_start = (seconds_per_hour * int(start_hour) + (seconds_per_minute * int(start_minute)) + float(start_minute))
total_seconds_stop = (seconds_per_hour * int(stop_hour) + (seconds_per_minute * int(stop_minute)) + float(stop_minute))

# Calculate the difference between start and finish times    |  PRINTING ZERO??
complete_seconds = total_seconds_stop - total_seconds_start
print(complete_seconds)

# Use integer division (//) to get the number of whole hours
final_hours = int(complete_seconds // seconds_per_hour)

# Use integer division (//) to get the number of minutes beyond whole hours
final_minutes = int(complete_seconds // seconds_per_minute)

# Use the modulis operator to calculate the number of seconds beyond whole minutes
final_seconds = complete_seconds % seconds_per_minute
# Get remaining seconds as a float of 2 decminals ()
decimal_final = float(complete_seconds)
# Display the results to the user

print(f'0{final_hours}:{final_minutes}:{decimal_final:.2f}')
