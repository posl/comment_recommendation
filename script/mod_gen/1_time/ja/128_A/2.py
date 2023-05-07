def main():
    # A = 林檎の数
    # P = 林檎の欠片の数
    A, P = map(int, input().split())
    # 林檎の数 * 3 + 林檎の欠片の数
    # // 2 で 林檎の欠片 * 2 でアップルパイの数
    print((A * 3 + P) // 2)

if __name__ == '__main__':
    main()