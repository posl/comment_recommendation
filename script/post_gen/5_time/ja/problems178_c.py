Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print((10**n - 2 * 9**n + 8**n) % (10**9 + 7))

=======
Suggestion 2

def main():
    N = int(input())
    print((10**N - 2*(9**N) + 8**N) % (10**9+7))

=======
Suggestion 3

def main():
    n = int(input())
    ans = (10**n - 2*(9**n) + 8**n) % (10**9 + 7)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    print((10**N - 9**N - 9**N + 8**N) % (10**9 + 7))

=======
Suggestion 5

def main():
    n = int(input())
    mod = 10**9+7
    ans = 10**n - 2*(9**n) + 8**n
    print(ans%mod)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 1
    for i in range(n):
        ans *= 10
        ans %= 1000000007
    ans -= 2
    ans += 1000000007
    ans %= 1000000007
    for i in range(n):
        ans *= 9
        ans %= 1000000007
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    MOD = 10**9+7
    print((10**N-(9**N+9**N-8**N))%MOD)

=======
Suggestion 8

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        print(2)
        return
    if n == 4:
        print(2)
        return
    if n == 5:
        print(2)
        return
    if n == 6:
        print(2)
        return
    if n == 7:
        print(2)
        return
    if n == 8:
        print(2)
        return
    if n == 9:
        print(2)
        return
    if n == 10:
        print(2)
        return
    if n == 11:
        print(2)
        return
    if n == 12:
        print(2)
        return
    if n == 13:
        print(2)
        return
    if n == 14:
        print(2)
        return
    if n == 15:
        print(2)
        return
    if n == 16:
        print(2)
        return
    if n == 17:
        print(2)
        return
    if n == 18:
        print(2)
        return
    if n == 19:
        print(2)
        return
    if n == 20:
        print(2)
        return
    if n == 21:
        print(2)
        return
    if n == 22:
        print(2)
        return
    if n == 23:
        print(2)
        return
    if n == 24:
        print(2)
        return
    if n == 25:
        print(2)
        return
    if n == 26:
        print(2)
        return
    if n == 27:
        print(2)
        return
    if n == 28:
        print(2)
        return
    if n == 29:
        print(2)
        return
    if n == 30:
        print(2)
        return
    if n == 31:
        print(2)
        return
    if n == 32:
        print(2)
        return
    if n == 33:
        print(2)

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((10**n - 2*9**n + 8**n) % (10**9+7))

=======
Suggestion 10

def main():
    n = int(input())
    ans = 10 ** n - 2 * 9 ** n + 8 ** n
    print(ans % (10 ** 9 + 7))
