def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 > 0:
            B.append(A[i+1] - A[i] - 1)
    B.sort()
    if B[0] == 0:
        print(0)
        exit()
    k = B[0]
    ans = 0
    for i in range(len(B)):
        ans += (B[i] + k - 1) // k
    print(ans)
