# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Store original values
x = a
y = b

# Find GCD using Euclidean Algorithm
while y != 0:
    x, y = y, x % y

gcd = x

# Find LCM
lcm = (a * b) // gcd

# Display results
print("GCD =", gcd)
print("LCM =", lcm)