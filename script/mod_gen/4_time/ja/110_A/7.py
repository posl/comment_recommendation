def main():
    # 標準入力受け取り
    a, b, c = map(int, input().split())
    # 出力
    print(max(a + b + c, a + b * c, a * b + c, a * b * c))

if __name__ == '__main__':
    main()