def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    B = [A[0] - 1]
    for i in range(1, M):
        B.append(A[i] - A[i - 1] - 1)
    B.append(N - A[M - 1])
    B.sort()
    if B[-1] == 0:
        print(0)
        return
    k = B[-1]
    ans = 1
    for i in range(M):
        ans += (A[i] - 1) // k
        ans += (N - A[i]) // k
    print(ans)
    return
