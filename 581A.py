r ,b= [int(i) for i in input().split(" ")]

min_=min(r,b)
max_=max(r,b)

print(min_,(max_-min_)//2)