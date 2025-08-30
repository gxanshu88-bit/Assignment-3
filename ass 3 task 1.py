def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    print("The factorial of n is ",result)    
n=int(input("Enter the number :"))
fact(n)