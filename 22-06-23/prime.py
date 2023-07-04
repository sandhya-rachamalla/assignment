a=int(input("enter a nm in lower range"))
b=int(input("ener a num in upper range"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            print(i,"is not a prime")
            break
    else:
        print(i,"is prime")
