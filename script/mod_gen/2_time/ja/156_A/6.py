def main():
    #入力
    n, r = map(int, input().split())
    #出力
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))

if __name__ == '__main__':
    main()