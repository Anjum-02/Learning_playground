a=input("enter a string")
i=0
j=len(a)-1
while i<=j:
    if a[i]!=a[j]:
        print("is not a palindrome")
        break

    else:
        i=i+1
        j=j-1
        print("is a palindrome")


