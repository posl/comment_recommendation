def main():
    #入力
    A,B,C,D,E = map(int,input().split())
    #フルハウスかどうかの判定
    if (A==B and B==C and D==E) or (A==B and C==D and D==E):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()