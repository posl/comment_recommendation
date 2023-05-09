def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1つ目の区間のビット単位ORを取っておく
    A0 = A[0]
    for i in range(1, N):
        A0 = A0 | A[i]
    # 2つ目の区間のビット単位ORを取っておく
    A1 = A[-1]
    for i in range(N-2, -1, -1):
        A1 = A1 | A[i]
    # 1つ目の区間のビット単位ORと2つ目の区間のビット単位ORのビット単位XORを取っておく
    A01 = A0 ^ A1
    # 1つ目の区間のビット単位ORと2つ目の区間のビット単位ORのビット単位XORの最小値を出力する
    print(min(A01, A0, A1))

if __name__ == '__main__':
    main()