def main():
    #入力
    AB,BC,CA = map(int,input().split())
    #面積
    S = int((AB*BC)/2)
    #出力
    print(S)

if __name__ == '__main__':
    main()