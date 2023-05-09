def f(m, a):
    return sum([m % i for i in a])
N = int(input())
a = [int(i) for i in input().split()]
l = 0
r = 10 ** 9
while r - l > 1:
    m = (l + r) // 2
    if f(m, a) >= f(m + 1, a):
        r = m
    else:
        l = m
print(f(r, a))
