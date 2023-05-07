def main():
    # 入力
    n, a, b = map(int, input().split())
    # 処理
    if a == 0 or b == 0:
        print(0)
    else:
        if a > b:
            print((n//(a+b))*a + min(n%(a+b), a))
        else:
            print((n//(a+b))*b + min(n%(a+b), b))

if __name__ == '__main__':
    main()