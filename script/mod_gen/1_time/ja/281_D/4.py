def main():
    #入力
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #処理
    #Aの要素をDで割った余りを取り出す
    A = [a%D for a in A]
    #Aの要素をDで割った余りを集計する
    #Aの要素の最大値は100なので、100を超える余りはない
    #余りの数は100個なので、余りの数を100個の要素に持つリストを作成
    #余りが0の場合は、0の要素に1を加算
    #余りが1の場合は、1の要素に1を加算
    #余りが2の場合は、2の要素に1を加算
    #余りが3の場合は、3の要素に1を加算
    #...
    #余りが99の場合は、99の要素に1を加算
    #余りが100の場合は、0の要素に1を加算
    #余りが101の場合は、1の要素に1を加算
    #余りが102の場合は、2の要素に1を加算
    #...
    #余りが199の場合は、99の要素に1を加算
    #余りが200の場合は、0の要素に1を加算
    #余りが201の場合は、1の要素に1を加算
    #余りが202の場合は、2の要素に1を加算
    #...
    #余りが299の場合は、99の要素に1を加算
    #余りが300の場合は、0の要素に1を加算
    #...
    #余りが399の場合は、99の要素に1を加算
    #余りが400の場合は、0の要素に1を加算

if __name__ == '__main__':
    main()