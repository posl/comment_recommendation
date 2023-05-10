def main():
    A_x,A_y = map(int, input().split())
    B_x,B_y = map(int, input().split())
    C_x,C_y = map(int, input().split())
    D_x,D_y = map(int, input().split())
    #print(A_x,A_y,B_x,B_y,C_x,C_y,D_x,D_y)
    #A,B,C,Dの頂点を結ぶ直線の傾きを求める
    #傾きが同じならば、同一直線上にあることになるので、凸ではない
    #傾きが違うならば、凸である
    if (B_y-A_y)*(C_x-B_x) == (C_y-B_y)*(B_x-A_x):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()