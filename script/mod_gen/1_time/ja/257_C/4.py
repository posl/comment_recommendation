def main():
    N = int(input())
    S = input()
    W = list(map(int,input().split()))
    # 体重の降順に並び替え
    W = sorted(W,reverse=True)
    #print(W)
    # 体重の降順に並び替えたときの、Sの0と1の数をカウント
    # 0の数が0のとき、すべての人が大人
    # 0の数がNのとき、すべての人が子供
    # 0の数がN/2のとき、体重の降順で半分が子供、半分が大人
    # 0の数がN/2+1のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+2のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+3のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+4のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+5のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+6のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+7のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+8のとき、体重の降順で半分が大人、半分が子供
    # 0の数がN/2+9のとき、体重の降順で

if __name__ == '__main__':
    main()