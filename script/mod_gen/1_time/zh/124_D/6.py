def solve():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S = [int(s) for s in S]
    # print(S)
    # print(K)
    # print(N)
    cnt = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            cnt += 1
    # print(cnt)
    ans = cnt + 2 * K
    if ans > N - 1:
        ans = N - 1
    print(ans)

if __name__ == '__main__':
    solve()