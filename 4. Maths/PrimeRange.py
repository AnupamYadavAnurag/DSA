n1 = int(input("Enter the first no. : "))
n2 = int(input("Enter the second no. : "))
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i)