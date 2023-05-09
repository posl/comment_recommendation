def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] < B[N-i-1]:
            ans += A[i]
            X -= 1
        else:
            ans += B[N-i-1]
            X -= 1
    if X > 0:
        ans += X * B[0]
    print(ans)
