from datetime import datetime
now=datetime.now()
current_time=now.strftime("%H:%M:%S:%MS")
print("Loop Start time", current_time)
count=0
while(count<=1000):
 print(count)
 count=count+1

print("Loop End time", current_time)
