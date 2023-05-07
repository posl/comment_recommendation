def main():
    #入力
    N = int(input())
    #出力
    if N >= -2147483648 and N < 2147483648:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    main()