Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(1, M // N + 1):
        if M % i == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    ans = 0
    for i in range(1, M + 1):
        if M % i == 0 and i <= M // N:
            ans = i
    print(ans)

=======
Suggestion 5

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    print(M//N)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    #MをNで割ったあまりを求める
    mod = M % N
    #MをNで割った商を求める
    div = M // N
    #MをNで割ったあまりが0の場合は、MをNで割った商が答えとなる
    if mod == 0:
        print(div)
    #MをNで割ったあまりが0でない場合は、MをNで割った商の数だけMをNで割ったあまりを1ずつ足す
    else:
        print(div + 1)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())

    # MをNで割った余りが0なら、最大公約数はM/N
    if M % N == 0:
        print(M // N)
        return

    # MをNで割った余りが0でないなら、最大公約数はM/Nの整数部分
    # つまり、MをNで割った商
    else:
        print(M // N)
