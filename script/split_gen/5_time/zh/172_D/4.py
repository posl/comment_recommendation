def f(x):
    result = 0
    for i in range(1, x+1):
        if x % i == 0:
            result += 1
    return result
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i * f(i)
print(sum)
