# Input from user
n = int(input("Enter a number: "))

factorial = 1

# Calculate factorial
for i in range(1, n + 1):
    factorial *= i

# Display result
print("Factorial of", n, "is", factorial)