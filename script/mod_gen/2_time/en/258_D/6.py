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
        if X == 1:
            ans += A[i]
            break
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    else:
        ans += B[-1] * X
    print(ans)

if __name__ == '__main__':
    main()