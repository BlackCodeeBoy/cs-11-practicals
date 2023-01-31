x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
result = x
for i in range(2, n+1):
    if i % 2 == 0:
        result += (x**i/i)
    else:
        result += -(x**i/i)
print(result)
