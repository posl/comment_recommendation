def main():
    #入力
    x,y,z = map(int, input().split())
    #操作
    x,y = y,x
    x,z = z,x
    #出力
    print(x,y,z)

if __name__ == '__main__':
    main()