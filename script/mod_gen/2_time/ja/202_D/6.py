def main():
    # A, B, K = map(int, input().split())
    A, B, K = 30, 30, 118264581564861424
    ans = ""
    for i in range(A+B):
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        # A + B - 1 個の a と b からなる文字列のうち、A - 1 個の a と B 個の b からなる文字列の総数
        if K <= comb(A + B - 1, A - 1):
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= comb(A + B, A)
    print(ans)

if __name__ == '__main__':
    main()