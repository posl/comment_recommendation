def main():
    #入力
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    #跳ねる回数
    count = 0
    #跳ねる位置
    pos = 0
    #跳ねる回数をカウント
    for i in range(N):
        pos += L[i]
        if pos > X:
            break
        count += 1
    #跳ねる回数を出力
    print(count + 1)

if __name__ == '__main__':
    main()