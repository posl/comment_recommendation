def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = set()
for i in a:
    for j in range(i, m + 1, i):
        s.add(j)
s = list(s)
s.sort()
print(len(s))
for i in s:
    print(i)
