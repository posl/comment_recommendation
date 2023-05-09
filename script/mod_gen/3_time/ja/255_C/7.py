def main():
    X, A, D, N = map(int, input().split())
    # X, A, D, N = map(int, input().split())
    # print(X, A, D, N)
    # X, A, D, N = 6, 2, 3, 3
    # X, A, D, N = 0, 0, 0, 1
    # X, A, D, N = 998244353, -10, -20, 30
    # X, A, D, N = -555555555555555555, -1000000000000000000, 1000000, 1000000000000
    # 1. AからXまでの差分を求める
    diff = X - A
    # print(diff)
    # 2. AからXまでの差分をDで割った商と余りを求める
    # 商をq、余りをrとする
    q, r = diff // D, diff % D
    # print(q, r)
    # 3. 余りが0の場合、qがN以下の場合はqを出力する
    if r == 0 and q <= N:
        print(q)
        return
    # 4. 余りが0でない場合、q+1がN以下の場合はq+1を出力する
    if r != 0 and q + 1 <= N:
        print(q + 1)
        return
    # 5. それ以外の場合は-1を出力する
    print(-1)

if __name__ == '__main__':
    main()