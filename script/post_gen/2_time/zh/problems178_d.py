Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(10 ** n - 2 * 9 ** n + 8 ** n)

=======
Suggestion 2

def main():
    n = int(input())
    print((10**n - 2*9**n + 8**n) % (10**9 + 7))

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(2)
        return
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。

    # 两个序列{0,9}和{9,0}满足所有条件。


    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。

    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。

    # 两个序列{0,9}和{9,0}满足所有条件。
    # 两个序列{0,9}和{9,0}满足所有条件。

    # 两个序列{0,9

=======
Suggestion 5

def solve():
    MOD = 10**9+7
    N = int(input())
    ans = pow(10,N,MOD) - 2*pow(9,N,MOD) + pow(8,N,MOD)
    ans %= MOD
    print(ans)

=======
Suggestion 6

def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        return (10 * 9 * (pow(10, n-2, 10**9+7) - pow(9, n-2, 10**9+7)) + 10 * pow(9, n-2, 10**9+7)) % (10**9+7)

=======
Suggestion 7

def solve():
    N = int(input())
    if N == 1:
        print(0)
        return
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))

solve()

=======
Suggestion 8

def main():
    n = int(input())
    print((pow(10,n,10**9+7) - pow(9,n,10**9+7) - pow(9,n,10**9+7) + pow(8,n,10**9+7))%(10**9+7))

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((10 ** n - 9 ** n - 9 ** n + 8 ** n) % (10 ** 9 + 7))
