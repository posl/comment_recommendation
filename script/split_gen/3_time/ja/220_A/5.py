def main():
    # A,B,Cの入力
    A,B,C = map(int,input().split())
    # Cの倍数を格納するリスト
    C_multiple = []
    # Cの倍数をリストに格納
    for i in range(A,B+1):
        if i % C == 0:
            C_multiple.append(i)
    # Cの倍数がない場合
    if len(C_multiple) == 0:
        print(-1)
    # Cの倍数がある場合
    else:
        print(C_multiple[0])
