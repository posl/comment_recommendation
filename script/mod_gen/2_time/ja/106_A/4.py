def main():
    # 入力
    a, b = map(int, input().split())
    # 出力
    print(a*b-(a+b-1))

if __name__ == '__main__':
    main()