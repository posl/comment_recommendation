def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        # A個のaとB個のbからなる文字列の総数をS個とする
        S = 0
        # A-1個のaとB個のbからなる文字列の総数をS1個とする
        S1 = 0
        # A個のaとB-1個のbからなる文字列の総数をS2個とする
        S2 = 0
        # A-1個のaとB-1個のbからなる文字列の総数をS3個とする
        S3 = 0
        # A-1個のaとB個のbからなる文字列の総数をS1個とする
        S1 = 1
        for i in range(A-1):
            S1 *= (A+B-1-i)
            S1 //= (i+1)
        # A個のaとB-1個のbからなる文字列の総数をS2個とする
        S2 = 1
        for i in range(B-1):
            S2 *= (A+B-1-i)
            S2 //= (i+1)
        # A-1個のaとB-1個のbからなる文字列の総数をS3個とする
        S3 = 1
        for i in range(A+B-2):
            S3 *= (A+B-2-i)
            S3 //= (i+1)
        S = S1 + S2
        if K <= S1:
            ans += "a"
            A -= 1
        elif K <= S:
            ans += "b"
            B -= 1
            K -= S1
        else:
            ans += "a"
            A -= 1
            K -= S
    if A == 0:
        ans += "b"*B
    else:
        ans += "a"*A
    print
