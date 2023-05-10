def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    B = []
    for i in range(M):
        if i == 0:
            B.append(A[i]-1)
        else:
            B.append(A[i]-A[i-1]-1)
        if i == M-1:
            B.append(N-A[i])
    B.sort()
    if B[-1] == 0:
        print(0)
        return
    k = B[-1]
    ans = 0
    for i in range(M):
        if B[i] > 0:
            ans += -(-B[i]//k)
    print(ans)
