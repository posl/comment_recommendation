def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
a = set(map(int, input().split()))
ans = set(range(1, m + 1))
for i in a:
    ans = ans - set(range(i, m + 1, i))
print(len(ans))
for i in ans:
    print(i)
