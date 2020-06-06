n,k= [int(i) for i in input().split(" ")]
remaining_minutes = 240 - k
count=0
i=1
while remaining_minutes>0:
	remaining_minutes-=i*5

	if remaining_minutes<0:
		break
	else:
		i+=1
		count+=1

	# print(remaining_minutes,count)

if (count)<n:
	if count==0:
		print(0)
	else:
		print(count)
else:
	print(n)


