def f(x):
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    return sum
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i * f(i)
print(sum)
