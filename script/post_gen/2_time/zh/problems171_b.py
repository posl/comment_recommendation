Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 2

def main():
    # 读取输入
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # 排序
    p.sort()
    # 输出
    print(sum(p[:k]))

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    print(sum(p[0:k]))

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    sum = 0
    for i in range(K):
        sum += p[i]
    print(sum)
