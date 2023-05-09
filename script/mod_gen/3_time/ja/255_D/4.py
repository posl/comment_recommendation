def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # 0 から 10^9 までの数値の出現回数を数える
    count = [0] * (10**9 + 1)
    for a in A:
        count[a] += 1
    # 0 から 10^9 までの数値の、それまでの数値の出現回数の累積和を求める
    cumsum = [0] * (10**9 + 1)
    for i in range(1, 10**9 + 1):
        cumsum[i] = cumsum[i-1] + count[i-1]
    # 0 から 10^9 までの数値の、それまでの数値の出現回数の累積和を求める
    cumsum2 = [0] * (10**9 + 1)
    for i in range(1, 10**9 + 1):
        cumsum2[i] = cumsum2[i-1] + cumsum[i]
    for x in X:
        # 0 から x までの数値の出現回数の累積和を求める
        cumsum3 = [0] * (x + 1)
        for i in range(1, x + 1):
            cumsum3[i] = cumsum3[i-1] + count[i]
        # 0 から x までの数値の、それまでの数値の出現回数の累積和を求める
        cumsum4 = [0] * (x + 1)
        for i in range(1, x + 1):
            cumsum4[i] = cumsum4[i-1] + cumsum3[i]
        # 0 から x までの数値の、それまでの数値の出現回数の累積和を求める
        cumsum5 = [

if __name__ == '__main__':
    main()