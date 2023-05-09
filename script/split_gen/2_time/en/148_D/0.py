def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    ans = 0
    for i in range(1, n):
        if a[i] == a[i-1]+1:
            continue
        if a[i] > a[i-1]+1:
            print(-1)
            return
        ans += a[i-1]-a[i]+1
    print(ans)
