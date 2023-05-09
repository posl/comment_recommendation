def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #昇順に並べ替えることが出来るかどうかを判定する。
    #N-K+1個のグループに分け、各グループの最大値を比較する。
    #最大値が昇順に並ぶならば、昇順に並べ替えることが出来る。
    #N-K+1個のグループに分けることで、N-K個の間隔があるので、
    #各グループの最大値を比較することで、N-K個の間隔の最大値を比較することが出来る。
    #グループの数
    group = N-K+1
    #グループの最大値を格納するリスト
    max_list = []
    #各グループの最大値を求める
    for i in range(group):
        max_list.append(max(A[i:i+K]))
    #グループの最大値が昇順に並ぶかどうかを判定
    if max_list == sorted(max_list):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()