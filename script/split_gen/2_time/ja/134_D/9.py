def main():
    N = int(input())
    A = list(map(int, input().split()))
    #2で割った余りが0の箱をリストに格納
    zero_box = []
    for i in range(N):
        if A[i] == 0:
            zero_box.append(i+1)
    #2で割った余りが1の箱をリストに格納
    one_box = []
    for i in range(N):
        if A[i] == 1:
            one_box.append(i+1)
    #2で割った余りが0の箱の個数と1の箱の個数の差が1以上なら-1を出力
    if abs(len(zero_box) - len(one_box)) >= 2:
        print(-1)
        exit()
    #2で割った余りが0の箱の個数が1多い場合
    if len(zero_box) - len(one_box) == 1:
        print(len(zero_box))
        for i in range(len(zero_box)):
            print(zero_box[i])
    #2で割った余りが1の箱の個数が1多い場合
    elif len(zero_box) - len(one_box) == -1:
        print(len(one_box))
        for i in range(len(one_box)):
            print(one_box[i])
    #2で割った余りが0の箱の個数と1の箱の個数が同じ場合
    else:
        print(len(zero_box))
        for i in range(len(zero_box)):
            print(zero_box[i])
