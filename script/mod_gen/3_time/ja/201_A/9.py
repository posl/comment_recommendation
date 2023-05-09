def main():
    #入力
    a,b,c = map(int,input().split())
    #出力
    if (a==b==c) or (a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()