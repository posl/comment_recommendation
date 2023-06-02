Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))

main()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))

=======
Suggestion 3

def main():
    n,k = map(int,input().split())

    while True:
        if n<k:
            break
        else:
            n = n%k
            if n>k:
                n = k-n
    print(n)
main()

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    if n < k:
        print(n)
    else:
        print(n % k)

=======
Suggestion 5

def main():
    # 读入输入
    n, k = map(int, input().split())
    # 计算最小值
    print(min(n % k, k - n % k))

=======
Suggestion 6

def problem161_c():
    n,k = map(int,input().split())
    while n >= k:
        n = n % k
    print(n)

=======
Suggestion 7

def solution(n,k):
    if n == 0:
        return 0
    else:
        return min(n%k, k - n%k)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    n = n%k
    print(min(n,k-n))

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(N%K if N%K<K else abs(N%K-K))

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    if (n%k == 0):
        print(0)
    else:
        print(1)
