def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 2:
        print(a[0])
    else:
        ans = a[0]
        for i in range(1, n - 1):
            ans = gcd(ans, a[i])
        print(ans)
