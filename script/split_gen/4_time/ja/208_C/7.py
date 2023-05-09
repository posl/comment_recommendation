def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        cnt += 1
        ans[i] = K // cnt
        if i == N - 1:
            break
        if K // cnt < K // (cnt + 1):
            K -= (K // cnt) * cnt
            for j in range(i + 1):
                ans[j] += K // (i + 1)
            K -= (K // (i + 1)) * (i + 1)
    for i in range(N):
        print(ans[A.index(A[i])])
