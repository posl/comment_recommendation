def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for s, c in sc:
        if ans[s-1] != -1 and ans[s-1] != c:
            print(-1)
            exit()
        ans[s-1] = c
    if N > 1 and ans[0] == 0:
        print(-1)
        exit()
    if N > 1 and ans[0] == -1:
        ans[0] = 1
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print("".join(map(str, ans)))
