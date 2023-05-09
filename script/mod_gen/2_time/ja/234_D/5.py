def main():
    #入力
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #K番目に大きい値を求める関数
    def kth_largest_value(P, K):
        #K番目に大きい値を求める
        P.sort()
        return P[-K]
    #K番目に大きい値を求める
    for i in range(K, N+1):
        print(kth_largest_value(P[:i], K))

if __name__ == '__main__':
    main()