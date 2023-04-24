Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, A = map(int, input().split())
    print(K % N + A - 1 if K % N + A - 1 <= N else K % N + A - 1 - N)

=======
Suggestion 2

def main():
    N, K, A = map(int, input().split())
    if K % N == 0:
        print(A)
    else:
        print((A + K % N - 1) % N + 1)

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    print((A + K - 1) % N + 1)

=======
Suggestion 4

def main():
    #入力
    N, K, A = map(int, input().split())
    #出力
    print((A + K - 2) % N + 1)

=======
Suggestion 5

def main():
    n,k,a = map(int,input().split())
    print((a+k-2)%n+1)

=======
Suggestion 6

def main():
    N,K,A = map(int,input().split())
    print((A+K-2)%N+1)

=======
Suggestion 7

def main():
    #入力
    n, k, a = map(int, input().split())
    #処理
    if k % n == 0:
        print(a)
    else:
        print((a + k % n - 1) % n + 1)

=======
Suggestion 8

def solve():
    n,k,a = map(int,input().split())
    print((a+k-2)%n+1)
solve()
