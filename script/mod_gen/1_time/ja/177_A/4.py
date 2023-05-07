def main():
    #入力
    D, T, S = map(int, input().split())
    #処理
    if D <= T * S:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()