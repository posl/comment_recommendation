Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    while N > K:
        N -= (K - 1)
        ans += 1
    print(ans + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > K:
        N -= (K-1)
        count += 1
    print(count+1)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if (n-1) % (k-1) == 0:
        print((n-1)//(k-1))
    else:
        print((n-1)//(k-1)+1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > 0:
        N -= K - 1
        count += 1
    print(count)

=======
Suggestion 5

def main():
    # 標準入力から N, K を取得する
    n, k = map(int, input().split())
    # 標準入力から A を取得する
    a = list(map(int, input().split()))
    # A をソートする
    a.sort()
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素の最小値を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素の最小値を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素の最小値を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素の最小値を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の先頭から K 個の要素の最小値を求める
    max = a[n-k:n]
    # A の先頭から K 個の要素の最小値を求める
    min = a[0:k]
    # A の

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_a = min(a)
    if min_a == 1:
        if n%k == 0:
            print(n//k)
        else:
            print(n//k+1)
    else:
        if (n-1)%(k-1) == 0:
            print((n-1)//(k-1))
        else:
            print((n-1)//(k-1)+1)

main()

=======
Suggestion 7

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    if (N - K) % (K - 1) == 0:
        ans += (N - K) // (K - 1)
    else:
        ans += (N - K) // (K - 1) + 1
    print(ans + 1)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print((N - 2) // (K - 1) + 1)
