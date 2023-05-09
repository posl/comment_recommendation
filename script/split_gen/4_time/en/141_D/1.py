def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] // 2**m
        if a[i] % 2**m != 0:
            m -= 1
        if m == -1:
            break
    print(ans)
