def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(C[i] - i, 0)
        ans %= 10 ** 9 + 7
    print(ans)

if __name__ == '__main__':
    solve()