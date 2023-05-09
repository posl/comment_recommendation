def main():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]
    # 処理
    cnt = 0
    for s in S:
        if s == "For":
            cnt += 1
    # 出力
    if cnt > N // 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()