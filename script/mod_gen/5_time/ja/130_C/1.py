def main():
    w,h,x,y = map(int,input().split())
    # 重心を求める
    gx = w/2
    gy = h/2
    # 重心と点(x,y)を結ぶ直線で長方形を二つに分割した時の面積の小さい方を求める
    if gx == x and gy == y:
        print(w*h/2,1)
    else:
        print(w*h/2,0)

if __name__ == '__main__':
    main()