def main():
    # 入力
    K = int(input())
    # 処理
    ans = 0
    for i in range(1, K + 1):
        if i % 2 == 0:
            for j in range(1, K + 1):
                if j % 2 == 1:
                    ans += 1
    # 出力
    print(ans)
main()

if __name__ == '__main__':
    main()