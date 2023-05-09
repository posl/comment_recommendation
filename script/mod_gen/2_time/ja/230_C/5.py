def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # Q-P+1行出力せよ。
    for i in range(Q-P+1):
        # 各行は # と . のみからなる長さ S-R+1 の文字列であり、
        # i 行目の文字列の j 番目の文字が
        # # であることは (P+i-1,R+j-1) が黒く塗られていることを、
        # . であることは (P+i-1,R+j-1) が白く塗られていることをさす。
        for j in range(S-R+1):
            x = P+i-1
            y = R+j-1
            if (A <= x <= N-B+1) and (B <= y <= N-A+1):
                print('#', end='')
            elif (A <= x <= N-B+1) and (N-A+1 <= y <= B-1):
                print('#', end='')
            elif (N-B+1 <= x <= A-1) and (B <= y <= N-A+1):
                print('#', end='')
            elif (N-B+1 <= x <= A-1) and (N-A+1 <= y <= B-1):
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main()