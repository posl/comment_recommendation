def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(N):
        ans = ans * (a[i] - i) % (10**9 + 7)
        if ans == 0:
            break
    print(ans)
solve()

if __name__ == '__main__':
    solve()