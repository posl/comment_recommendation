def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] > B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    for i in range(X):
        ans += B[i]
    print(ans)

if __name__ == '__main__':
    main()