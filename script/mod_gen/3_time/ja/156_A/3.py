def main():
    #入力
    N, R = map(int, input().split())
    #出力
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

if __name__ == '__main__':
    main()