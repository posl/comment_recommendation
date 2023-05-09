def main():
    # 入力
    N = int(input())
    # 出力
    if N <= 54:
        print('AGC' + str(N + 1).zfill(3))
    else:
        print('AGC' + str(N).zfill(3))

if __name__ == '__main__':
    main()