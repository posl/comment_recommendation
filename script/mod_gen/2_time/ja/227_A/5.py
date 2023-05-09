def main():
    # 入力
    n,k,a = map(int,input().split())
    # 出力
    print((a + k - 1) % n + 1)

if __name__ == '__main__':
    main()