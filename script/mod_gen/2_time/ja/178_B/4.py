def main():
    #入力
    a,b,c,d = map(int,input().split())
    #処理
    if a >= 0 and c >= 0:
        print(a*d)
    elif a >= 0 and c < 0:
        if d >= 0:
            print(a*d)
        else:
            print(a*c)
    elif a < 0 and c >= 0:
        if b >= 0:
            print(b*d)
        else:
            print(a*d)
    elif a < 0 and c < 0:
        if b >= 0:
            if d >= 0:
                print(max(a*d,b*c))
            else:
                print(max(a*c,b*c))
        else:
            print(max(a*c,b*d))

if __name__ == '__main__':
    main()