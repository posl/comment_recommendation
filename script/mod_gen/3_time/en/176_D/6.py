def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())
    #print(H,W)
    #print(C_h,C_w)
    #print(D_h,D_w)
    #print(S)
    #A: 1マス移動
    #B: 5*5の範囲内で移動
    #A or Bを繰り返す
    #Aの場合は、上下左右に移動可能
    #

if __name__ == '__main__':
    main()