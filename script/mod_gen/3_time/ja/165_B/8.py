def main():
    #入力
    X = int(input())
    #初期値
    Y = 100
    #処理
    for i in range(1, 10**10):
        Y = Y * 101 // 100
        if Y >= X:
            print(i)
            break

if __name__ == '__main__':
    main()