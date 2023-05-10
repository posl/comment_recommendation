def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    P = 0
    Q = 0
    R = 0
    S = 0
    min_diff = 10**9
    for i in range(1, N-2):
        P += A[i-1]
        Q = 0
        for j in range(i+1, N-1):
            Q += A[j-1]
            R = 0
            for k in range(j+1, N):
                R += A[k-1]
                S = A_sum - P - Q - R
                max_val = max(P, Q, R, S)
                min_val = min(P, Q, R, S)
                min_diff = min(min_diff, max_val - min_val)
    print(min_diff)
