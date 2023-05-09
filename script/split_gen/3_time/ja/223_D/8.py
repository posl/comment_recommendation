def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * N
    for a, b in AB:
        if ans[a - 1] == 0 and ans[b - 1] == 0:
            ans[a - 1] = b
            ans[b - 1] = a
        elif ans[a - 1] == 0:
            ans[a - 1] = b
        elif ans[b - 1] == 0:
            ans[b - 1] = a
        else:
            print(-1)
            return
    for i in range(N):
        if ans[i] == 0:
            ans[i] = i + 1
    print(*ans)
