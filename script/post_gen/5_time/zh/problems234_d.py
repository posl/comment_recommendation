Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1])[-k])

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # print(n, k, p)
    for i in range(k-1, n):
        # print(i, k, n)
        print(max(p[i-k+1:i+1]))

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1],reverse=True)[k-1])

=======
Suggestion 4

def max_k_value(p, k):
    max_k = max(p[:k])
    for i in range(k, len(p)):
        if p[i] > max_k:
            max_k = p[i]
    return max_k

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    p = P[:K]
    p.sort()
    print(p[-1])
    for i in range(N-K):
        p.remove(P[i])
        p.append(P[i+K])
        p.sort()
        print(p[-1])

=======
Suggestion 6

def get_max_k_num(nums, k):
    # 从大到小排序
    nums.sort(reverse=True)
    return nums[k-1]

=======
Suggestion 7

def main():
    # 读取输入
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)
    #print(type(n), type(k), type(p))
    #print(len(p))
    #print(p[0])
    #print(p[1])
    #print(p[2])
    #print(p[3])
    #print(p[4])
    #print(p[5])
    #print(p[6])
    #print(p[7])
    #print(p[8])
    #print(p[9])
    #print(p[10])

    #p = list(map(int, input().split()))
    #print(p)
    #print(type(p))
    #print(len(p))
    #print(p[0])
    #print(p[1])
    #print(p[2])
    #print(p[3])
    #print(p[4])
    #print(p[5])
    #print(p[6])
    #print(p[7])
    #print(p[8])
    #print(p[9])
    #print(p[10])

    # 问题陈述
    # 给出一个(1,2,...,N)的排列组合P=(P_1,P_2,...,P_N)和一个正数K。
    # 对于每个i=K,K+1,...,N,求出以下结果。
    # P的前i项中的第K个最大值。
    #
    # 限制条件
    # 1 ≦ k ≦ n ≦ 5 × 10^5
    # (P_1,P_2,...,P_N)是(1,2,...,N)的一个排列组合。
    # 输入的所有数值都是整数。
    #
    # 输入
    # 输入是由标准输入给出的，格式如下：
    # N K
    # P_1 P_2 ...P_N
    #
    # 输出
    # 对于每个i=K，K+1，...，N，按照这个顺序，打印问题陈述中的指定值，用换行符分隔。

    #print(p)
    #print(type(p

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    for i in range(K-1,N):
        print(sorted(P[:i+1],reverse=True)[K-1])
