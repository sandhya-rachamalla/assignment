n=5
k=n-1
for i in range(n):
    for j in range(k):
        print(' ',end=" ")
    k-=1
    print()
    for l in range(i+1):
        print("*",end=" ")
    print()
