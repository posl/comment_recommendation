def f(x):
    return x
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += f(i)
print(sum % 998244353)
