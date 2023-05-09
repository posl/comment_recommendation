def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > ans:
            ans += 1
    print(N - ans)
solve()

if __name__ == '__main__':
    solve()