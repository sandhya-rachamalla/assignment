n=int(input("enter a num"))
count=0
while n>0:
    n=n//10
    count+=1
print("the no.of digits in a num",count)
