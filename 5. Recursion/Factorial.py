# n! = n* (n-1)*(n-2)*....*1
# 4! = 4*3*2*1 = 24
def factorial(n):
    result = 1
    for i in range (2,n+1):
        result *=i
    return result
print(factorial(3))