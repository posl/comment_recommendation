def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum_a = [0]
    for i in range(N):
        sum_a.append(sum_a[i] + A[i])
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum_a[j] - sum_a[i] >= K:
                ans += 1
    print(ans)
