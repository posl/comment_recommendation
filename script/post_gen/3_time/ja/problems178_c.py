Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print((pow(10,N,10**9+7)-pow(9,N,10**9+7)-pow(9,N,10**9+7)+pow(8,N,10**9+7))%(10**9+7))

=======
Suggestion 2

def main():
    N = int(input())
    MOD = 10**9+7
    print((pow(10,N,MOD)-pow(9,N,MOD)-pow(9,N,MOD)+pow(8,N,MOD))%MOD)

=======
Suggestion 3

def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    ans = (10 ** N - 2 * (9 ** N) + 8 ** N) % MOD
    print(ans)

=======
Suggestion 4

def main():
    mod = 10**9 + 7
    N = int(input())
    ans = (10**N - 2*(9**N) + 8**N) % mod
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    mod = 10**9 + 7
    print((10**N - 2*(9**N) + 8**N) % mod)

=======
Suggestion 6

def main():
    N = int(input())
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))

=======
Suggestion 7

def main():
    # 入力
    N = int(input())
    # 出力
    print((10**N - 2*9**N + 8**N) % (10**9 + 7))

=======
Suggestion 8

def main():
    N = int(input())
    MOD = 10**9+7
    print((9**N + 7**N - 8**N)%MOD)

=======
Suggestion 9

def main():
    N = int(input())
    # 0と9を含む数列は、0から9のどの数字を含むかによって、組み合わせが決まる
    # 0から9のどの数字を含むかは、N-1個の区切りを入れる組み合わせの数と同じ
    # 0から9のどの数字を含むかを求めるには、N-1個の空白を入れる組み合わせの数を求めればいい
    # 0から9のどの数字を含むかを求めるには、0から9のどの数字を含まないかを求めればいい
    # 0から9のどの数字を含まないかを求めるには、0から9のどの数字を含むかを求めればいい
    # 0から9のどの数字を含むかを求めるには、0から9のどの数字を含まないかを求めればいい
    # 0から9のどの数字を含まないかを求めるには、0から9のどの数字を含むかを求めればいい
    # 0から9のどの数字を含むかを求めるには、0から9のどの数字を含まないかを求めればいい
    # 0から9のどの数字を含まないかを求めるには、0から9のどの数字を含むかを求めればいい
    # 0から9のどの数字を含むかを求めるには、0から9のどの数字を含まないかを求めればいい
    # 0から9のどの数字を含まないかを求めるには、0から9のどの数字を含むかを求めればいい
    # 0から9のどの数字を含
