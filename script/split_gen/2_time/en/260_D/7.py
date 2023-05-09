def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    K = min(K, N - K)
    ans = [-1] * N
    for i in range(N):
        if ans[i] == -1:
            j = i
            cnt = 0
            while ans[j] == -1:
                ans[j] = i + 1
                j = P[j] - 1
                cnt += 1
            if cnt > K:
                for l in range(N):
                    if ans[l] == i + 1:
                        ans[l] = -1
    print(*ans, sep = "
")
