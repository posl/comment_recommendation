Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k,n+1):
        print(sorted(p[:i])[-k])

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))

    for i in range(k-1,n):
        print(sorted(p[0:i+1])[k-1])

=======
Suggestion 3

def main():
    N,K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K-1,N):
        print(sorted(P[:i+1])[-K+1])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # print(n, k, p)
    # print(p[0:3])
    # print(p[0:2])
    # print(p[0:1])
    # print(p[0:0])

    for i in range(k-1,n):
        print(max(p[i-k+1:i+1]))

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    for i in range(k-1,n):
        print(sorted(p[:i+1],reverse=True)[k-1])

=======
Suggestion 6

def max_k(a,k):
    max = 0
    for i in range(k):
        if a[i] > max:
            max = a[i]
    return max

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    #print(p[:k])
    for i in range(k-1,n):
        print(sorted(p[:i+1],reverse=True)[k-1])

=======
Suggestion 8

def main():
    #读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    #print(n, k, p)

    #解决方案1
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[-k])

    #解决方案2
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i], reverse=True)[k-1])

    #解决方案3
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[i-k])

    #解决方案4
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i], reverse=True)[k-1])

    #解决方案5
    #问题陈述中的指定值
    #for i in range(k, n+1):
    #    print(sorted(p[:i])[i-k])

    #解决方案6
    #问题陈述中的指定值
    for i in range(k, n+1):
        print(sorted(p[:i], reverse=True)[k-1])
