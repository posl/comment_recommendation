def main():
    #入力
    X = int(input())
    #出力
    print((X//500)*1000 + ((X%500)//5)*5)

if __name__ == '__main__':
    main()