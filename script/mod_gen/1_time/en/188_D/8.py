def main():
    N, C = map(int, input().split())
    #各サービスの開始日と終了日をリストに格納
    start = []
    end = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        start.append(a)
        end.append(b)
    #開始日と終了日をソート
    start.sort()
    end.sort()
    #各サービスの開始日と終了日をインデックスにして、開始日の数をカウント
    #終了日の数を引くことで、開始日と終了日の積集合をカウント
    start_count = [0] * (10 ** 9 + 1)
    end_count = [0] * (10 ** 9 + 1)
    for i in range(N):
        start_count[start[i]] += 1
        end_count[end[i]] += 1
    #開始日と終了日のカウントを累積和
    sc = [0]
    ec = [0]
    for i in range(10 ** 9 + 1):
        sc.append(sc[i] + start_count[i])
        ec.append(ec[i] + end_count[i])
    #開始日と終了日の積集合をカウント
    #開始日と終了日の積集合が0の場合、サービスは一つも使っていない
    #開始日と終了日の積集合が1以上の場合、サービスを使っている
    #開始日と終了日の積集合が2以上の場合、サービスを使っている
    #開始日と終了日の積集合が3以上の場合、サービスを使っている
    #開始日と終了日の積集合が4以上の場合、サービスを使っている
    #開始日と終了日の積集合が5以上

if __name__ == '__main__':
    main()