def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    C.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if A[i] < C[-1]:
            ans += C[-1]
            C.pop()
        else:
            ans += A[i]
    print(ans)
