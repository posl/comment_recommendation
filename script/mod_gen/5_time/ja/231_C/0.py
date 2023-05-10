def main():
    #入力
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    #処理
    A.sort()
    ans = [0] * Q
    for i in range(Q):
        ans[i] = N - (len(A) - bisect.bisect_left(A, X[i]))
    #出力
    for i in range(Q):
        print(ans[i])

if __name__ == '__main__':
    main()