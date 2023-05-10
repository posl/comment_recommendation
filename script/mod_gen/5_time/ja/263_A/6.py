def main():
    # データ入力
    a,b,c,d,e = map(int,input().split())
    # フルハウスの条件を満たすかどうか判定
    if ((a == b and b == c and d == e) or
        (a == b and c == d and d == e)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()