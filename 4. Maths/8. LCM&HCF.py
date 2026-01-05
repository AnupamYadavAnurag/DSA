a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# HCF
x, y = a, b
while y != 0:
    x, y = y, x % y
hcf = x

# LCM
lcm = (a * b) // hcf

print("HCF =", hcf)
print("LCM =", lcm)
