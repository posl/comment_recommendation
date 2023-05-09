def main():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    ans = 0
    for i in range(N):
        if X > 1:
            ans += A[i]
            X -= 1
        else:
            break
    ans += B[i] * X
    print(ans)
main()
