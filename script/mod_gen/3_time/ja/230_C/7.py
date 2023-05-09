def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1行目の出力
    for j in range(R, S+1):
        if A <= j <= B:
            print('#', end='')
        else:
            print('.', end='')
    print()
    # 2行目以降の出力
    for i in range(P+1, Q+1):
        # 1列目の出力
        if A <= i <= B:
            print('#', end='')
        else:
            print('.', end='')
        # 2列目以降の出力
        for j in range(R+1, S+1):
            if (A <= i <= B) and (A <= j <= B):
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main()