n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")
