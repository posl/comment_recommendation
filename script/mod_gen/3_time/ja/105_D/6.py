def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 累積和
    B = [0]
    for i in range(N):
        B.append(B[i] + A[i])
    # print(B)
    # あまりの個数
    C = [0] * M
    for i in range(N + 1):
        C[B[i] % M] += 1
    # print(C)
    # あまりの個数から組み合わせを計算
    for i in range(M):
        ans += C[i] * (C[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()