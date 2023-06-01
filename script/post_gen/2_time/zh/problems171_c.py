Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problems171_b():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list.sort()
    print(sum(p_list[:K]))

=======
Suggestion 4

def main():
    # 读取输入
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    # 排序
    p.sort()

    # 计算结果
    ans = 0
    for i in range(k):
        ans += p[i]

    # 输出结果
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = sorted(map(int, input().split()))
    print(sum(p[:k]))

=======
Suggestion 6

def main():
    N,K=map(int,input().split())
    p=list(map(int,input().split()))
    p.sort()
    print(sum(p[0:K]))
