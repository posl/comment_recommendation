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
    for i in range(N-1, -1, -1):
        if X > 0:
            if A[i] >= B[i]:
                ans += B[i]
                X -= 1
            else:
                ans += A[i]
                X -= 1
        else:
            ans += A[i]
    print(ans)
