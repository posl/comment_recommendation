def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        # A 個の a と B 個の b からなる文字列の総数
        S = 1
        for i in range(A + B):
            S *= (i + 1)
        for i in range(A):
            S //= (i + 1)
        for i in range(B):
            S //= (i + 1)
        # A 個の a と B 個の b からなる文字列のうち、辞書順で K 番目のものを求める
        if K <= S // 2:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= S // 2
    print(ans)

if __name__ == '__main__':
    main()