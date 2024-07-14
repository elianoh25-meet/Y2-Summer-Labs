import random
temperatures=[]
for i in range(7):
	temperatures.append(random.randint(26,41))
	days_of_the_week=["Sunday","Monday","tuesday","wednsday","thirsday","friday","saturday"]
good_days_count=[]
for i in range (7):
	if temperatures[i]%2==0:
		good_days_count.append(days_of_the_week[i])
low=0
high=0
for i in range(7):
	if temperatures[i]<temperatures[low]:
		low=i
	if temperatures[i]>temperatures[high]:
		high=i
lowest_temp = temperatures[low]
lowest_temp_day = days_of_the_week[low]
highest_temp = temperatures[high]
highest_temp_day = days_of_the_week[high]
avg=0
for i in temperatures:
	avg=avg+i
avg=avg/7
above_avg=[]
for i in range(7):
	if temperatures[i] > avg:
		above_avg.append(days_of_the_week[i])
for i in range(7):
	print(days_of_the_week[i], " - ", temperatures[i])
print("the good days for shelly is-", len(good_days_count))
print("the most  hot temperature was-", highest_temp,"on",highest_temp_day)
print("the most cold temperature was- ", lowest_temp,"on", lowest_temp_day)
print("the avreg temp: ", avg)
print("the days with above average are: ", above_avg)