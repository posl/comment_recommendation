def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = [-1] * N
    for i in range(N):
        P[i] -= 1
    for i in range(N):
        if ans[i] != -1:
            continue
        now = i
        cnt = 0
        while ans[now] == -1:
            ans[now] = cnt
            now = P[now]
            cnt += 1
        if cnt <= K:
            continue
        now = i
        while cnt > K:
            ans[now] = -1
            now = P[now]
            cnt -= 1
    for i in range(N):
        print(ans[i] + 1)
