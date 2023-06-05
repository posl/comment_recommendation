def f(n):
    if n % 15 == 0:
        return 0
    elif n % 3 == 0:
        return 1
    elif n % 5 == 0:
        return 2
    else:
        return 3
n = int(input())
sum = 0
for i in range(n):
    sum += i + 1 - f(i+1)
print(sum)
