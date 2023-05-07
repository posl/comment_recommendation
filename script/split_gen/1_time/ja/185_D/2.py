def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 > 0:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
        return
    C = min(B)
    ans = 0
    for i in range(len(B)):
        ans += (B[i] + C - 1) // C
    print(ans)
