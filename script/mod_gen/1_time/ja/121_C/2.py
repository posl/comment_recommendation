def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 価格の安い順にソート
    A, B = zip(*sorted(zip(A, B)))
    # 累積和
    B = [0] + list(B)
    for i in range(1, N + 1):
        B[i] += B[i - 1]
    # 価格の安い順に買っていく
    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * (M - B[i - 1])
            break
        else:
            ans += A[i] * B[i]
    print(ans)

if __name__ == '__main__':
    main()