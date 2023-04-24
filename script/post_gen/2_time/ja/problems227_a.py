Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, A = map(int, input().split())
    if K % N == 0:
        print(A)
    else:
        print((A + K % N - 1) % N + 1)

=======
Suggestion 2

def main():
    N, K, A = map(int, input().split())
    print((A + K - 1) % N + 1)

=======
Suggestion 3

def main():
    n, k, a = map(int, input().split())
    print((a + k - 1) % n + 1)

=======
Suggestion 4

def main():
    N,K,A = map(int,input().split())
    print((A+K-2)%N+1)

=======
Suggestion 5

def main():
    N, K, A = map(int, input().split())
    print((A-1 + K) % N + 1)

=======
Suggestion 6

def main():
    # 入力
    n,k,a = map(int,input().split())
    # 出力
    print((a + k - 1) % n + 1)
