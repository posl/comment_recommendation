def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += a[i]
        else:
            ans += min(a[i], a[i-1])
    print(ans)
