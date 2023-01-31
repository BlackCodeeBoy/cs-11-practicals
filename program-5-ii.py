x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
result = 0

for i in range(n+1):
    if i % 2 == 0:
        result += x**i
    else:
        result += -(x**i)
print(result)
