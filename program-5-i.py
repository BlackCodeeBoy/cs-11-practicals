x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
result = 0
for i in range(n+1):
    result += x**i
print(result)
