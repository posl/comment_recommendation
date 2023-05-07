def main():
    #入力
    n, k, a = map(int, input().split())
    #処理
    if k % n == 0:
        print(a)
    else:
        print((a + k % n - 1) % n + 1)

if __name__ == '__main__':
    main()