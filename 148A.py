# «One dragon. Two dragon. Three dragon», — the princess was counting.
 # She had trouble falling asleep, and she got bored of counting lambs when she was nine.

# However, just counting dragons was boring as well, so she entertained 
# herself at best she could. Tonight she imagined that all dragons were 
# here to steal her, and she was fighting them off. Every k-th dragon got punched 
# in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door./ 
# Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th
 # dragon to call her mom, and he withdrew in panic.

# How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?aa

import pdb

k = int(input())
l= int(input())
m = int(input())
n= int(input())
d= int(input())
count=0
arr=[]
for i in range(1,d+1):
	# pdb.set_trace()
	if i%k==0:
		count+=1
		continue

	if i%l==0:
		count+=1
		continue

	if i%m==0:
		count+=1
		continue

	if i%n==0:
		count+=1
		continue
print(count)
