def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
    else:
        k = min(B)
        ans = 0
        for i in range(len(B)):
            ans += (B[i]+k-1)//k
        print(ans)
