#time
minutes = float(input('Nhập phút: '))
seconds = float(input('Nhập giây: '))
total_seconds = minutes * 60 + seconds
total_minutes = minutes + seconds/60
hours = total_seconds / 3600
print("Total seconds:", total_seconds)

#distance
kilometers = float(input('Kilometers: '))
miles = kilometers/1.61
print("Miles: ",miles)

# pace
pace_minutes = total_minutes/miles
pace_seconds = total_seconds/miles
speed_mph = miles / hours
print("Average pace: ", pace_minutes, "minutes per mile")
print("Average pace: ",pace_seconds, "seconds per mile")
print("Average speed:", speed_mph, "miles per hour")
