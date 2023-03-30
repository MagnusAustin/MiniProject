#while loop
result = 1
n=5
while n > 0:
    result *= n
    n -= 1
print(result)

#forloop
result = 1
for i in range(1, 5+1):
    result *= i
print(result)

#whileloop
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
result = factorial(5)
print(result) # Output: 120
