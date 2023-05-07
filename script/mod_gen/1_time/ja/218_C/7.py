def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    #print("S:", S)
    #print("T:", T)
    # Sの#の座標を取得
    Sx = []
    Sy = []
    for i, s in enumerate(S):
        for j, c in enumerate(s):
            if c == "#":
                Sx.append(i)
                Sy.append(j)
    #print("Sx:", Sx)
    #print("Sy:", Sy)
    # Tの#の座標を取得
    Tx = []
    Ty = []
    for i, t in enumerate(T):
        for j, c in enumerate(t):
            if c == "#":
                Tx.append(i)
                Ty.append(j)
    #print("Tx:", Tx)
    #print("Ty:", Ty)
    # Sの#の座標とTの#の座標を比較
    # 一致していれば、Yes
    # 一致していなければ、No
    if len(Sx) == len(Tx):
        if Sx[0] == Tx[0] and Sy[0] == Ty[0]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()