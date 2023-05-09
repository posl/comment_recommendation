def main():
    #入力
    A, B, C, D, E, F, X = map(int, input().split())
    #高橋君の距離
    Takahashi = (A + C) * (X // (A + C)) + min(A, X % (A + C))
    #青木君の距離
    Aoki = (D + F) * (X // (D + F)) + min(D, X % (D + F))
    #出力
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()