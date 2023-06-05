def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    c = [0] * (n + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = n
    for i in range(1, n + 1):
        if c[i] >= 2:
            ans -= c[i]
    for i in range(n):
        print(ans)
        x = a[i]
        c[x] -= 1
        if c[x] >= 2:
            ans -= 1
