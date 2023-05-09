def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
    #print(A_sum)
    ans = 10**9
    for i in range(1, N-1):
        for j in range(i+1, N):
            P = A_sum[i]
            Q = A_sum[j] - A_sum[i]
            R = A_sum[N] - A_sum[j]
            S = A_sum[N] - A_sum[i]
            #print(P, Q, R, S)
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)
