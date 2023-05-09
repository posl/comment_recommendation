def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    ans = 0
    for i in range(N):
        if A[i] < B[N - 1 - i]:
            ans += A[i]
            X -= 1
            if X == 0:
                break
        else:
            ans += B[N - 1 - i]
            X -= 1
            if X == 0:
                break
    if X > 0:
        ans += B[N - 1 - i] * X
    print(ans)
