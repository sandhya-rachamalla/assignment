a=int(input("enter a num:"))
temp=a
rev_no=0
while temp>0:
    rem=temp%10
    rev_no=(rev_no*10)+rem
    temp=temp//10
print("reverse of",a,"is",rev_no)
