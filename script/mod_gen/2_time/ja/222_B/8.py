def main():
    # 入力
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    # 処理
    cnt = 0
    for i in range(n):
        if a[i] < p:
            cnt += 1
    # 出力
    print(cnt)

if __name__ == '__main__':
    main()