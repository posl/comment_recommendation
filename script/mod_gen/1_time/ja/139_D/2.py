def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i-1
    print(ans)

if __name__ == '__main__':
    solve()