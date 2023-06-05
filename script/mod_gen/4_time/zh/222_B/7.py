def solve():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if a[i] < p:
            ans += 1
    print(ans)

if __name__ == '__main__':
    solve()