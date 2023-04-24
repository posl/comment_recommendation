Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((max(A, B, C, D, E) + 9) // 10 * 10)

=======
Suggestion 2

def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    print(10 * ((A + 9) // 10 + (B + 9) // 10 + (C + 9) // 10 + (D + 9) // 10 + (E + 9) // 10) - max(A, B, C, D, E))

=======
Suggestion 3

def main():
    a, b, c, d, e = [int(input()) for _ in range(5)]
    print(((a + 9) // 10 + (b + 9) // 10 + (c + 9) // 10 + (d + 9) // 10 + (e + 9) // 10) * 10 - 9)

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((10 - max(A, B, C, D, E) % 10) % 10 + max(A, B, C, D, E))

main()

Here is the code for the problem 124 A. Button.

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += a + (10 - a % 10) % 10
    ans += b + (10 - b % 10) % 10
    ans += c + (10 - c % 10) % 10
    ans += d + (10 - d % 10) % 10
    ans += e + (10 - e % 10) % 10
    ans -= max(a, b, c, d, e) + (10 - max(a, b, c, d, e) % 10) % 10
    print(ans)

=======
Suggestion 7

def solve():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += ((a + 9) // 10) * 10
    ans += ((b + 9) // 10) * 10
    ans += ((c + 9) // 10) * 10
    ans += ((d + 9) // 10) * 10
    ans += ((e + 9) // 10) * 10
    ans -= max(a % 10, b % 10, c % 10, d % 10, e % 10)
    print(ans)

solve()

=======
Suggestion 8

def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]
    N = 5
    ans = 0
    ans = max(A, B, C, D, E)
    ans = ans + (ans - 1) // 9 * 10
    print(ans)

=======
Suggestion 9

def main():
    # input
    As = [int(input()) for _ in range(5)]

    # compute
    # 10の倍数に切り上げる
    As = [((a+9)//10)*10 for a in As]
    # 最小値を求める
    m = min(As)
    # 最小値の10の倍数の差分を求める
    d = m - As[0]
    # 最小値の10の倍数に合わせる
    As = [a+d for a in As]
    # 最大値を求める
    M = max(As)
    # 最大値に合わせる
    As = [M for _ in range(5)]

    # output
    print(sum(As))

=======
Suggestion 10

def main():
    # Put your code here
    pass
