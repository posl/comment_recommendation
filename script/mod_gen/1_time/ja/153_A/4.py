def main():
    #入力
    H, A = map(int, input().split())
    #出力
    print((H + A - 1) // A)

if __name__ == '__main__':
    main()