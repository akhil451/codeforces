t = int(input())
for i in range(t):
    n = int(input())
    # print("(n%2)%2",n,n%2,(n/2)%2)
    if n ==2 :
        print("NO")
    elif (n/2)%2==1:
        print("NO")
    else :
        print("YES")
        odd=1
        for i in range(n):
            if (i+1)<=(n/2):
                print(2*(i+1),end=" ")
                last = 2*(i+1)
            else:
                
                if (i+1)<n:
                    
                    print(odd,end=" ")
                    odd+=2
                if i==(n-1):
                    print(int(last+(n/2)-1))