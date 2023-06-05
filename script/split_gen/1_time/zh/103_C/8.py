def f(m):
    sum = 0
    for i in range(0, N):
        sum += m % a[i]
    return sum
N = int(input())
a = list(map(int, input().split()))
max = 0
for i in range(0, N):
    if a[i] > max:
        max = a[i]
min = f(max)
for i in range(max - 1, 0, -1):
    if f(i) <= min:
        min = f(i)
    else:
        print(f(i + 1))
        break
else:
    print(f(1))
