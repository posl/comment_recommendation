def main():
    #入力
    K = int(input())
    #初期化
    H = 21
    M = 0
    #計算
    M += K
    if M > 59:
        H += M // 60
        M = M % 60
    if H > 23:
        H = H % 24
    #出力
    print(str(H) + ":" + str(M).zfill(2))

if __name__ == '__main__':
    main()