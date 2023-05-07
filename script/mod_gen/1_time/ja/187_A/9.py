def main():
    #入力
    A, B = map(int, input().split())
    #S(A)を求める
    S_A = 0
    while A > 0:
        S_A += A % 10
        A //= 10
    #S(B)を求める
    S_B = 0
    while B > 0:
        S_B += B % 10
        B //= 10
    #S(A)とS(B)のうち大きい方を出力
    if S_A > S_B:
        print(S_A)
    else:
        print(S_B)

if __name__ == '__main__':
    main()