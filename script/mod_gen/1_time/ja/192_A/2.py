def main():
    #入力
    X = int(input())
    #出力
    if X % 100 == 0:
        print(0)
    else:
        print(100 - X % 100)

if __name__ == '__main__':
    main()