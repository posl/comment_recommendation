def f(x):
    i = 1
    sum = 0
    while i * i <= x:
        if x % i == 0:
            sum += i
            if i * i != x:
                sum += x / i
        i += 1
    return sum - x
n = int(raw_input())
sum = 0
for i in range(1, n + 1):
    sum += i * f(i)
print sum
