def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    ans = 0
    for i in range(N):
        if M < B[i]:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

if __name__ == '__main__':
    main()