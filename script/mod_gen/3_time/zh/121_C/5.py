def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N):
        if M == 0:
            break
        if B[i] >= M:
            ans += A[i] * M
            M = 0
        else:
            ans += A[i] * B[i]
            M -= B[i]
    print(ans)

if __name__ == '__main__':
    main()