def main():
    # 入力
    N = int(input())
    H = list(map(int, input().split()))
    # ここに処理を書く
    max_h = H[0]
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    # 出力
    print(max_h)

if __name__ == '__main__':
    main()