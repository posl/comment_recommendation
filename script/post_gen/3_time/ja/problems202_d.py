Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            ab = 1
            for i in range(1, A + B):
                ab *= i
            for i in range(1, A):
                ab //= i
            for i in range(1, B):
                ab //= i
            if K <= ab:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= ab
    print(ans)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            # A 個の a と B 個の b からなる長さ A + B の文字列の総数を S 個とおいたとき、1 ≦ K ≦ S
            # A 個の a と B 個の b からなる長さ A + B - 1 の文字列の総数を S' 個とおいたとき、1 ≦ K ≦ S'
            # となるため、S - S' 個の文字列のうち、最初の a は aab..b である。
            # つまり、辞書順で K 番目の文字列の先頭の文字は、a と b のうち K 番目に小さい文字である。
            # また、a と b のうち K 番目に小さい文字が a であれば、その文字を選択した場合には a が 1 つ増える。
            # つまり、K 番目の文字列の先頭の文字が a である場合には、K は S - S' 個の文字列のうち、最初の a が aab..b であるものを除いたものになる。
            # また、a と b のうち K 番目に小さい文字が b であれば、その文字を選択した場合には b が 1 つ増える。
            # つまり、K 番目の文字列の先頭の文字が b である場合には、K は S' 個の文字列のうち

=======
Suggestion 4

def main():
    A, B, K = map(int, input().split())
    s = ''
    while A + B > 0:
        if A == 0:
            s += 'b'
            B -= 1
        elif B == 0:
            s += 'a'
            A -= 1
        else:
            # a が先頭にくる場合
            if K <= comb(A + B - 1, A - 1):
                s += 'a'
                A -= 1
            # b が先頭にくる場合
            else:
                s += 'b'
                K -= comb(A + B - 1, A - 1)
                B -= 1
    print(s)

=======
Suggestion 5

def solve(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A

    if K <= comb(A + B - 1, A - 1):
        return 'a' + solve(A - 1, B, K)
    else:
        return 'b' + solve(A, B - 1, K - comb(A + B - 1, A - 1))

=======
Suggestion 6

def combination(n, r):
    if n == 0 or r == 0 or n == r:
        return 1
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)

=======
Suggestion 7

def solve():
    A,B,K = map(int,input().split())
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            if A >= B:
                if K <= A*B:
                    ans += "a"
                    A -= 1
                else:
                    ans += "b"
                    B -= 1
                    K -= A*B
            else:
                if K <= A*B:
                    ans += "b"
                    B -= 1
                else:
                    ans += "a"
                    A -= 1
                    K -= A*B
    print(ans)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    A, B, K = map(int, input().split())
    ans = ''
    while A > 0 and B > 0:
        if A > B:
            if K <= A:
                ans += 'a'
                A -= 1
            else:
                ans += 'b'
                K -= A
                B -= 1
        else:
            if K <= B:
                ans += 'b'
                B -= 1
            else:
                ans += 'a'
                K -= B
                A -= 1
    while A > 0:
        ans += 'a'
        A -= 1
    while B > 0:
        ans += 'b'
        B -= 1
    print(ans)

=======
Suggestion 10

def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        # aを先頭にする場合の数
        cnt = comb(A + B - 1, A - 1)
        if cnt >= K:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
            K -= cnt
    ans += "a" * A
    ans += "b" * B
    print(ans)
