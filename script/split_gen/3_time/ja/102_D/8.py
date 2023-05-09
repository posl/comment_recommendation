def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 4:
        print(max(A) - min(A))
    else:
        ans = 10**10
        for i in range(3):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N - 1):
                    P = sum(A[:i + 1])
                    Q = sum(A[i + 1:j + 1])
                    R = sum(A[j + 1:k + 1])
                    S = sum(A[k + 1:])
                    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
        print(ans)
