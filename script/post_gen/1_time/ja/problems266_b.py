Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print((N % 998244353 - 998244353) % 998244353)

=======
Suggestion 2

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 3

def main():
    N = int(input())
    print((N%998244353))

=======
Suggestion 4

def main():
    N = int(input())
    print((N % 998244353) - 998244353)

=======
Suggestion 5

def main():
    n = int(input())
    print((n-1)%998244353+1)

=======
Suggestion 6

def main():
    N = int(input())
    mod = 998244353
    print(N % mod)

=======
Suggestion 7

def main():
    n = int(input())
    # 0以上998244353未満の整数xを求める
    # N-xは998244353の倍数
    # つまり、N-xを998244353で割った余りが0になるxを求める
    # 余りが0になるxは、Nを998244353で割った余り
    print(n%998244353)
