def main():
    W,H,x,y = list(map(int,input().split()))
    #最大値を達成する分割の方法が複数あるかも判定する
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

if __name__ == '__main__':
    main()