def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #最小値を取る数に変換
    for i in range(N):
        A[i] -= 1
    #数列の長さをKで割った余りを求める
    mod = N % K
    #余りが0のときは、Kで割った数を求める
    if mod == 0:
        mod = N // K
    #余りが0でないときは、Kで割った数に1を足す
    else:
        mod = N // K + 1
    #余りを出力する
    print(mod)

if __name__ == '__main__':
    main()