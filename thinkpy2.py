import time
current_time = time.time()
total_seconds = int(current_time)
days = int(total_seconds//86400)
remaining_seconds =total_seconds%86400
hours = remaining_seconds//3600
remaining_seconds =remaining_seconds%3600
minutes =remaining_seconds//60
seconds = remaining_seconds%60
print("Days since epoch:", days)
print("Current time:", hours, ":", minutes, ":", seconds)
