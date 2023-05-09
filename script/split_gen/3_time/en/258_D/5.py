def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.append(0)
    B.append(0)
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
            if X <= 0:
                break
            A[i] = 0
            B[i] = 0
        else:
            ans += B[i]
            B[i] = 0
    if X > 0:
        A.append(A[N])
        B.append(B[N])
        A[N] = 0
        B[N] = 0
        A[N+1] = 0
        B[N+1] = 0
        A[N] = min(A[N], A[N+1])
        B[N] = min(B[N], B[N+1])
        A[N+1] = 0
        B[N+1] = 0
        ans += min(A[N], B[N]) * X
    print(ans)
