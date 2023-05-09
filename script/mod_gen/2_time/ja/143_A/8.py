def main():
    # A:窓の横幅,B:カーテンの横幅
    A, B = map(int, input().split())
    # 窓の横幅がカーテンの横幅より短い場合
    if A < B:
        print(0)
    # 窓の横幅がカーテンの横幅より長い場合
    else:
        print(A - B)

if __name__ == '__main__':
    main()