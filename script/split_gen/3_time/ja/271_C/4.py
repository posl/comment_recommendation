def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print(0)
        return
    ans = 1
    for i in range(1, N):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)
