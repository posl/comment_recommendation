Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    print(0 if n%k==0 else 1)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    print(int(N/K))

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    print(0 if N%K == 0 else 1)

=======
Suggestion 4

def problem105_a():
    n,k = input().split()
    n = int(n)
    k = int(k)
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    # 读取输入
    n, k = map(int, input().split())

    # 计算结果
    print(n % k)

=======
Suggestion 6

def main():
    #n,k=[int(i) for i in input().split()]
    n,k=map(int,input().split())
    print(0 if n%k==0 else 1)

=======
Suggestion 7

def problems105_a():
    n, k = map(int, input().split())
    print(0 if n % k == 0 else 1)
