Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    k = K // N
    r = K % N
    for i in range(N):
        if i < r:
            print(k + 1)
        else:
            print(k)

=======
Suggestion 2

def problems208_c(n, k, a):
    if k >= n:
        return [k // n for i in range(n)]
    else:
        a = sorted(a)
        b = [0 for i in range(n)]
        for i in range(k):
            b[a[i]-1] += 1
        return b

=======
Suggestion 3

def f(n,k,a):
    m = k//n
    b = [m for i in range(n)]
    c = [i for i in range(n)]
    d = list(zip(a,b,c))
    d.sort()
    for i in range(k%n):
        d[i] = (d[i][0],d[i][1]+1,d[i][2])
    d.sort(key=lambda x:x[2])
    for i in range(n):
        print(d[i][1])

n,k = map(int,input().split())
a = list(map(int,input().split()))
f(n,k,a)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    cnt = [0]*n
    for i in range(n):
        cnt[i] = k//n
    for i in range(k%n):
        cnt[i] += 1
    for i in range(n):
        print(cnt[a.index(a[i])])

=======
Suggestion 5

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [k//n]*n
    k%=n
    for i in range(k):
        ans[i]+=1
    for i in range(n):
        print(ans[a.index(a[i])])

=======
Suggestion 6

def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 排序
    a.sort()
    # 计算每个人的糖果
    candy = k // n
    # 余下的糖果
    remain = k % n
    # 计算每个人的糖果
    for i in range(n):
        if a[i] < remain:
            print(candy + 1)
        else:
            print(candy)

=======
Suggestion 7

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    a1=a[0]
    a2=a[1]
    if k>=n:
        for i in range(n):
            print(k//n)
    else:
        k1=k
        for i in range(n):
            if a[i]==a1:
                print(k1//n+1)
                k1-=1
            else:
                print(k1//n)

=======
Suggestion 8

def find_min(a):
    return min(a)

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = [k//n]*n
    for i in range(k%n):
        l[i] += 1
    for i in range(n):
        print(l[a.index(a[i])])

=======
Suggestion 10

def get_input():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    return N, K, a
