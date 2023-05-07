def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = []
    for i in range(M+1):
        if A[i] != 1:
            B.append(A[i]-A[i-1]-1)
    B.sort(reverse=True)
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += B[i]
    print(ans)
