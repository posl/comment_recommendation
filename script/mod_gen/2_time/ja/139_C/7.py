def main():
    #入力
    N = int(input())
    H = list(map(int, input().split()))
    #処理
    count = 0
    for i in range(1, N):
        if H[i - 1] >= H[i]:
            count += 1
        else:
            count = 0
    #出力
    print(count)

if __name__ == '__main__':
    main()