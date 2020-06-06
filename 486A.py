n = int(input())
# fn = [((-1)**n)*n for n in range(n+1)]
# print(fn)
# a = -1 
# l= (-1)**n
# s= sum((-1)**(k) * k for k in range(1, n + 1))
n_l = n%2
if n_l == 0:
	n_ = n//2
else:
	n_ = int(n//2 + ((-1)**n)*n)
print(n_)