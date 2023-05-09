def main():
    #入力
    A, B, T = map(int, input().split())
    #処理
    cnt = 0
    for i in range(1, T+1):
        if i % A == 0:
            cnt += B
    #出力
    print(cnt)

if __name__ == '__main__':
    main()