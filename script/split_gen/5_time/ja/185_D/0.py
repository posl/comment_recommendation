def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    B = []
    for i in range(1,M+1):
        if A[i] - A[i-1] -1 != 0:
            B.append(A[i] - A[i-1] -1)
    if len(B) == 0:
        print(0)
        return
    K = min(B)
    ans = 0
    for b in B:
        ans += (b + K - 1) // K
    print(ans)
