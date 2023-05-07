def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.append(0)
    B.append(0)
    A = sorted(A)
    B = sorted(B)
    ans = 0
    for i in range(N):
        if X >= A[i] + B[i]:
            ans += A[i] + B[i]
            X -= A[i] + B[i]
        else:
            ans += X
            break
    if X > 0:
        ans += min(A[N], B[N])
    print(ans)

if __name__ == '__main__':
    main()