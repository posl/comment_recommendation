def main():
    # 入力
    N, K = map(int, input().split())
    mod = 10**9 + 7
    # 処理
    # 青いボールを右端からi個取り除く場合の組み合わせ数
    # これを全てのiについて計算する
    # i個取り除く場合の組み合わせ数は、
    # (N-K+1)C(i) = (N-K+1)! / (i! * (N-K+1-i)!)
    # で求められる
    # ただし、i=0のときは、(N-K+1)C(0) = 1
    # それ以外のときは、(N-K+1)C(i) = (N-K+1)C(i-1) * (N-K+1-i) / i
    # となる
    # これらの値を計算する
    # また、(N-K+1)C(i)はmodで割った余りを求める
    # これは、iの最大値がKなので、
    # (N-K+1)! / (i! * (N-K+1-i)!) = (N-K+1) * (N-K+2) * ... * (N-K+1-i) / (1 * 2 * ... * i)
    # となるので、(N-K+1-i) / i のmodを求める
    # これは、pow(i, mod-2, mod)で求められる
    # これらを用いて、(N-K+1)C(i)を計算する
    # また、i=0のときは、1を代入する
    # これらの値を用いて、青いボールを右端からi個取り除く場合の組み合わせ数を計算する
    # これは、(N-K+1)C(i) * (K-1)C(i

if __name__ == '__main__':
    main()