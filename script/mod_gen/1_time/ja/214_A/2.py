def main():
    # 入力
    N = int(input())
    # 出力
    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    else:
        print(8)

if __name__ == '__main__':
    main()