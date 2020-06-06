k,n,w = [int(x) for x in input().split(" ")]
s = sum(range(w+1))
s=s*k
print(s)
if s>n:
    print(s-n)
else: 
    print(0)