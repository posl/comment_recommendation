def f(n):
    result = 0
    for i in range(1, n+1):
        if n%i == 0:
            result += i
    return result
n = int(input())
result = 0
for i in range(1, n+1):
    result += i*f(i)
print(result)
