Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    print(min(N%K, K-N%K))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    print(n%k if n%k < k else k - n%k)

=======
Suggestion 3

def solve(n,k):
    if k==1:
        return 0
    if n<k:
        return min(n,abs(n-k))
    return min(n%k,abs(n%k-k))

=======
Suggestion 4

def main():
    # 读取输入
    N, K = map(int, input().split())
    # 一次操作后的值
    N = N % K
    # 取两者的最小值
    print(min(N, abs(N-K)))

=======
Suggestion 5

def main():
    n , k = map(int, input().split())
    n = n % k
    print(min(n, k - n))

=======
Suggestion 6

def main():
    n, k = [int(x) for x in input().split()]
    print(min(n % k, k - n % k))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))

=======
Suggestion 8

def solve(n,k):
    if n == 0:
        return 0
    else:
        return min(n%k,k-n%k)
