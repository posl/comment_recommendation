def main():
    #入力
    a,b,c,d,e = map(int,input().split())
    #出力
    print("Yes" if (a==b==c and d==e) or (a==b and c==d==e) else "No")

if __name__ == '__main__':
    main()