def main():
    # 入力
    A, B, C, D, E, F = map(int, input().split())
    # 出力
    print((A*B*C-D*E*F) % 998244353)

if __name__ == '__main__':
    main()