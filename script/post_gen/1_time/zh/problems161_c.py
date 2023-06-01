Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, k):
    return min(n % k, k - (n % k))

=======
Suggestion 2

def solve(n,k):
    ans = n
    while True:
        if ans > abs(ans-k):
            ans = abs(ans-k)
        else:
            break
    return ans

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    if n==0:
        print(0)
    else:
        print(min(n%k,k-n%k))

=======
Suggestion 5

def main():
    n,k = list(map(int, input().split()))
    if n < k:
        print(n)
    else:
        print(min(n % k, k - n % k))

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    while n >= k:
        n = n % k
        if n == 0:
            print(0)
            return
    print(min(n, abs(k - n)))

=======
Suggestion 7

def main():
    # 读取输入
    n, k = map(int, input().split())

    # 计算答案
    print(min(n % k, k - n % k))

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    print(min(n%k, k-(n%k)))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(min(N%K, K-N%K))
