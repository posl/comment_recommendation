Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - A*(N//A)*(N//A+1)//2 - B*(N//B)*(N//B+1)//2 + A*B*(N//(A*B))*(N//(A*B)+1)//2)

=======
Suggestion 2

def main():
    N, A, B = map(int, input().split())
    print(N*(N+1)//2 - (A*(N//A)*(N//A+1)//2 + B*(N//B)*(N//B+1)//2 - A*B*(N//(A*B))*(N//(A*B)+1)//2))

=======
Suggestion 3

def main():
    N, A, B = map(int, input().split())
    ans = 0
    ans += (N // A) * (A * (A + 1) // 2)
    ans += (N // B) * (B * (B + 1) // 2)
    ans -= (N // (A * B)) * (A * B * (A * B + 1) // 2)
    ans -= (N // A) * (N // A + 1) // 2 * A
    ans -= (N // B) * (N // B + 1) // 2 * B
    ans += (N // (A * B)) * (N // (A * B) + 1) // 2 * A * B
    print(ans)

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    print((n // a) * (a + a * (n // a - 1)) // 2 + (n // b) * (b + b * (n // b - 1)) // 2 - (n // (a * b)) * (a * b + a * b * (n // (a * b) - 1)) // 2)

=======
Suggestion 5

def f(n, a, b):
    x = n // a
    y = n // b
    z = n // (a * b)
    return n * (n + 1) // 2 - x * (x + 1) // 2 * a - y * (y + 1) // 2 * b + z * (z + 1) // 2 * a * b

=======
Suggestion 6

def main():
    N, A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    if A == B:
        print(N // A)
    else:
        print((N // A) * (N // B) * (A + B) // 2)

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    # 1 から N までの整数のうち、A または B で割り切れない整数の和を求める
    # A で割り切れる整数の個数
    cntA = N // A
    # B で割り切れる整数の個数
    cntB = N // B
    # A と B で共通に割り切れる整数の個数
    cntAB = N // (A * B)
    # 1 から N までの整数のうち、A または B で割り切れない整数の個数
    cnt = N - cntA - cntB + cntAB
    print(cnt * (A + B) - cntAB * A * B)

=======
Suggestion 8

def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    #print(N//(A*B), N//A, N//B)
    print(N - N//A - N//B + N//(A*B))

=======
Suggestion 9

def main():
    N, A, B = map(int, input().split())

    def sum_div(n):
        return (n * (n + 1)) // 2

    def sum_div_A(n):
        return A * sum_div(n // A)

    def sum_div_B(n):
        return B * sum_div(n // B)

    def sum_div_AB(n):
        return (A * B) * sum_div(n // (A * B))

    def sum_div_not_AB(n):
        return sum_div(n) - sum_div_A(n) - sum_div_B(n) + sum_div_AB(n)

    print(sum_div_not_AB(N))
