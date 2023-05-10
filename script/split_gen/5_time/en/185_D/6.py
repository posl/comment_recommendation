def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0]
    for i in range(M):
        B.append(A[i] - A[i-1] - 1)
    B.append(N - A[M-1])
    B.sort()
    k = B[1]
    ans = 0
    for i in range(M+1):
        ans += (B[i] + k - 1) // k
    print(ans)
