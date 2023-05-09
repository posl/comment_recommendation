def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]
    #print(N, Q, A, K)
    # 1. 1, 2, 4, 8, 9, 10, 11, ... のように、Aの間隔の倍数の数列を作る
    # 2. 1.の数列にAを足す
    # 3. 2.の数列にKを足す
    # 4. 3.の数列に1を足す
    # 5. 4.の数列をソートする
    # 6. 5.の数列のK番目の要素を出力する
    B = [1]
    for i in range(N-1):
        B.append(B[i] + A[i+1] - A[i])
    #print(B)
    C = []
    for b in B:
        for k in K:
            C.append(b + k)
    #print(C)
    D = sorted(C)
    #print(D)
    for i in range(Q):
        print(D[i])

if __name__ == '__main__':
    main()