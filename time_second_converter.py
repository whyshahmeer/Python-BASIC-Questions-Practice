# Write a Python program to convert all units of time into seconds.


days = int(input("Days: "))
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

day_seconds = days * 86400
hour_seconds = hours * 3600
minute_seconds = minutes * 60

total_seconds = day_seconds + hour_seconds + minute_seconds + seconds

print(total_seconds)