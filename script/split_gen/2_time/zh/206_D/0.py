def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i + 1 > a[i]:
            ans += a[i]
        else:
            ans += a[i] - (i + 1)
    print(ans)
