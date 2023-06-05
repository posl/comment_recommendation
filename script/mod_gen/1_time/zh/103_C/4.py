def f(m):
    sum = 0
    for i in range(N):
        sum += m % a[i]
    return sum
N = int(input())
a = list(map(int, input().split()))
a.sort()
max = 0
for m in range(a[0], a[N - 1] * N, a[0]):
    if f(m) > max:
        max = f(m)
print(max)

if __name__ == '__main__':
    f()