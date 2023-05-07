def main():
    N, Q = map(int, input().split())
    S = input()
    query = [input().split() for _ in range(Q)]
    # 1の回数をカウント
    cnt = 0
    for q in query:
        if q[0] == '1':
            cnt += int(q[1])
    # 1の回数をNで割った余りを取得
    cnt %= N
    # 1の回数をNで割った余りをSから取得
    ans = S[cnt:] + S[:cnt]
    print(ans)
    # 2のクエリの場合は、Sから取得した文字列のインデックスを出力
    for q in query:
        if q[0] == '2':
            print(ans[int(q[1]) - 1])

if __name__ == '__main__':
    main()