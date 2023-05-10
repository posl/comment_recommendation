def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for i in range(M):
        s, c = sc[i]
        if ans[s - 1] == -1 or ans[s - 1] == c:
            ans[s - 1] = c
        else:
            print(-1)
            exit(0)
    if N != 1 and ans[0] == 0:
        print(-1)
        exit(0)
    if N == 1 and ans[0] == -1:
        print(0)
        exit(0)
    if N == 1 and ans[0] != -1:
        print(ans[0])
        exit(0)
    if ans[0] == 0:
        print(-1)
        exit(0)
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print(''.join(list(map(str, ans))))
