def main():
    # 读入
    k = int(input())
    # 7, 77, 777, ...の数列
    a = 7
    for i in range(1, 10**6):
        # Kの倍数になっているかをチェック
        if a % k == 0:
            print(i)
            exit()
        # 次の値を作る
        a = a * 10 + 7
    print(-1)

if __name__ == '__main__':
    main()