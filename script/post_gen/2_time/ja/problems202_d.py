Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    ans = ''
    while A > 0 or B > 0:
        if A == 0:
            ans += 'b'
            B -= 1
            continue
        if B == 0:
            ans += 'a'
            A -= 1
            continue
        if K > comb(A + B - 1, A - 1):
            ans += 'b'
            B -= 1
            K -= comb(A + B - 1, A - 1)
        else:
            ans += 'a'
            A -= 1
    print(ans)

=======
Suggestion 2

def main():
    A,B,K = map(int,input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            tmp = 1
            for i in range(1,A+B):
                tmp *= i
                if i == A:
                    tmp //= i
                    tmp //= B
            if K <= tmp:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= tmp
    print(ans)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())

    ans = ""
    while A > 0 or B > 0:
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if A == 0:
            ans += "b"
            B -= 1
            continue

        # a を先頭にする場合
        # A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(A-1)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1

=======
Suggestion 4

def f(A, B, K):
    if A == 0:
        return 'b' * B
    if B == 0:
        return 'a' * A
    if K <= C[A - 1][B]:
        return 'a' + f(A - 1, B, K)
    else:
        return 'b' + f(A, B - 1, K - C[A - 1][B])

A, B, K = map(int, input().split())
C = [[0] * (B + 1) for _ in range(A + 1)]

for i in range(A + 1):
    for j in range(B + 1):
        if i == 0 and j == 0:
            C[i][j] = 1
        elif i == 0:
            C[i][j] = C[i][j - 1]
        elif j == 0:
            C[i][j] = C[i - 1][j]
        else:
            C[i][j] = C[i - 1][j] + C[i][j - 1]

print(f(A, B, K))

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    a = "a"
    b = "b"
    if A == 0:
        print(b * B)
    elif B == 0:
        print(a * A)
    else:
        if A >= B:
            if K <= (A + B) * (A + B - 1) // 2 - (B - 1):
                print(a + main())
            else:
                print(b + main())
        else:
            if K <= (A + B) * (A + B - 1) // 2 - (A - 1):
                print(b + main())
            else:
                print(a + main())

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 and B > 0:
        if A > B:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            B -= 1
    if A > 0:
        ans += "a" * A
    else:
        ans += "b" * B
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    S = A + B
    ans = [0] * S
    for i in range(S):
        if A == 0:
            ans[i] = "b"
            B -= 1
        elif B == 0:
            ans[i] = "a"
            A -= 1
        else:
            if i == 0:
                if K <= comb(A + B - 1, A - 1):
                    ans[i] = "a"
                    A -= 1
                else:
                    ans[i] = "b"
                    B -= 1
                    K -= comb(A + B + 1, A)
            else:
                if ans[i - 1] == "a":
                    if K <= comb(A + B - 1, A - 1):
                        ans[i] = "a"
                        A -= 1
                    else:
                        ans[i] = "b"
                        B -= 1
                        K -= comb(A + B + 1, A)
                else:
                    if K <= comb(A + B - 1, A):
                        ans[i] = "a"
                        A -= 1
                        K -= comb(A + B + 1, A + 1)
                    else:
                        ans[i] = "b"
                        B -= 1
    print("".join(ans))

=======
Suggestion 9

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

=======
Suggestion 10

def main():
    A,B,K = map(int,input().split())
    ans = ''
    while A and B:
        if A*B < K:
            K -= A*B
            if A > B:
                ans += 'b'
                B -= 1
            else:
                ans += 'a'
                A -= 1
        else:
            if A > B:
                ans += 'a'
                A -= 1
            else:
                ans += 'b'
                B -= 1
    while A:
        ans += 'a'
        A -= 1
    while B:
        ans += 'b'
        B -= 1
    print(ans)
