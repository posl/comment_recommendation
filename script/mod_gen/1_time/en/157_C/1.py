def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
        S[i] -= 1 # 0-indexed
    if N == 1:
        if M == 0:
            print(0)
        else:
            print(C[0])
        return
    if M == 0:
        print(10**(N-1))
        return
    ans = [-1] * N
    for i in range(M):
        if ans[S[i]] == -1:
            ans[S[i]] = C[i]
        elif ans[S[i]] != C[i]:
            print(-1)
            return
    if ans[0] == 0:
        print(-1)
        return
    if ans[0] == -1:
        ans[0] = 1
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()