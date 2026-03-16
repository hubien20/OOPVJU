#the_volume_sphere
import math
r=5
n=(4/3)*math.pi*r**3
print("The volume sphere: ",n,"with ",5)

#price
price=24.95
discount=0.4
shipping_cots=3+(0.75*59)
Total=price*(1-discount)*60+shipping_cots
print("Total wholesale of 60 copies: ",Total)

#time 
start_time=6*3600+52*60
easy_pace=8*60+15
tempo_pace=3*(7*60+12)
finish_time=easy_pace*2+tempo_pace+start_time
hours=finish_time//3600
minutes=(finish_time%3600)//60
seconds=finish_time%60
print("Time get home for breakfast:", hours, ":", minutes, ":", seconds)
