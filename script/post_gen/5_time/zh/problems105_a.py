Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    n, k = map(int, input().split())

    # compute
    # n % k == 0
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def problems105_a():
    N, K = map(int, input().split())
    print(0 if N % K == 0 else 1)

=======
Suggestion 3

def main():
    # 读取输入
    n, k = map(int, input().split())
    # 计算结果
    ans = 0 if n % k == 0 else 1
    # 输出结果
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    print(0 if n%k==0 else 1)

=======
Suggestion 6

def func105_a():
    n,k = map(int,input().split())
    print(1 if n%k != 0 else 0)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    if n%k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 8

def read_input():
    return map(int, input().split())

=======
Suggestion 9

def problems105_a():
    n, k = map(int, input().split())
    print(n % k)
