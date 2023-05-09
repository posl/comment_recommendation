def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]
    # Aの各行の和を計算
    Asum = [0] * H1
    for i in range(H1):
        Asum[i] = sum(A[i])
    # Bの各行の和を計算
    Bsum = [0] * H2
    for i in range(H2):
        Bsum[i] = sum(B[i])
    # Aの各行の和とBの各行の和が一致しているかどうかを判定
    Asum.sort()
    Bsum.sort()
    if Asum == Bsum:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()