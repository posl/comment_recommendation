def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 1e18:
            print(-1)
            return
    print(ans)
