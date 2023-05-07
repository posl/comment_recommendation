def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1行目の出力
    for i in range(R, S + 1):
        if B - N <= i - B <= B - 1:
            print('#', end='')
        else:
            print('.', end='')
    print()
    # 2行目以降の出力
    for i in range(P + 1, Q + 1):
        # 1列目の出力
        if A - N <= i - A <= A - 1:
            print('#', end='')
        else:
            print('.', end='')
        # 2列目以降の出力
        for j in range(R + 1, S + 1):
            if A - N <= i - A <= A - 1 or B - N <= j - B <= B - 1:
                print('#', end='')
            else:
                print('.', end='')
        print()
