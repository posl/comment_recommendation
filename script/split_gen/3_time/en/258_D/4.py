def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    if X > 0:
        ans += X * B[N - 1]
    print(ans)
