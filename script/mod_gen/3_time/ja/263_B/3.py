def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if P[i] == N:
            ans += 1
            N = i + 1
    print(ans)

if __name__ == '__main__':
    solve()