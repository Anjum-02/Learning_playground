num=int(input("enter a number"))
fact=1
if num==0:
    print("the factorial of 0 is 1")

else:
    for i in range(1,num+1):
        fact=num*i
    print("the factorial of",num,"is",fact)