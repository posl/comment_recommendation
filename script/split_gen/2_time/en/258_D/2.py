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
        if A[i] < B[i]:
            ans += A[i] * X
            X -= 1
        else:
            break
    if X > 0:
        ans += B[i] * X
    print(ans)
