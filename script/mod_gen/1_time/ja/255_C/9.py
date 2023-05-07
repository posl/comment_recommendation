def main():
    X, A, D, N = map(int, input().split())
    # 1. Dが0の場合
    if D == 0:
        # 1.1. AとXが等しい場合
        if A == X:
            print(0)
        # 1.2. AとXが等しくない場合
        else:
            print(abs(X - A))
    # 2. Dが0でない場合
    else:
        # 2.1. AとXが等しい場合
        if A == X:
            print(0)
        # 2.2. AとXが等しくない場合
        else:
            # 2.2.1. XがAより小さい場合
            if X < A:
                #

if __name__ == '__main__':
    main()