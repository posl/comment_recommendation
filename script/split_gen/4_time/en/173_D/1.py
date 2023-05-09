def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    if n == 2:
        ans = a[0] + a[1]
    else:
        a.sort()
        ans = a[-1] + a[-2]
        for i in range(n - 3):
            ans += a[i]
    print(ans)
