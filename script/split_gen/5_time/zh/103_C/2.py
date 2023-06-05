def f(m, a):
    sum = 0
    for i in a:
        sum += m % i
    return sum
N = int(input())
a = list(map(int, input().split()))
max = 0
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            m = f(a[i] + a[j] + a[k], a)
            if m > max:
                max = m
print(max)
