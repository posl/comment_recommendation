def main():
    #入力
    W,H,x,y = map(int, input().split())
    #処理
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

if __name__ == '__main__':
    main()