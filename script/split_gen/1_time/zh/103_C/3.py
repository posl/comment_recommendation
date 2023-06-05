def f(m, a):
    sum = 0
    for i in a:
        sum += m % i
    return sum
N = int(input())
a = list(map(int, input().split()))
m = a[0]
for i in a:
    if i > m:
        m = i
print(f(m, a))
