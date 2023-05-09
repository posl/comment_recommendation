def main():
    # 文字列の入力
    p = list(map(int, input().split()))
    a = list(map(chr, range(97, 123)))
    ans = ''
    for i in p:
        ans += a[i-1]
    print(ans)

if __name__ == '__main__':
    main()