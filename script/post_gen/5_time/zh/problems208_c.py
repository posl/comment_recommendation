Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    num = 0
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[i] = k//n
    for i in range(n):
        if ans[i] > a[i]:
            num += ans[i] - a[i]
    for i in range(n):
        if num == 0:
            break
        if ans[i] > a[i]:
            if num > 0:
                ans[i] -= 1
                num -= 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    b=[0]*n
    for i in range(n):
        b[i]=k//n
    k%=n
    for i in range(k):
        b[i]+=1
    c=[0]*n
    for i in range(n):
        c[i]=a[i]
    c.sort()
    for i in range(n):
        for j in range(n):
            if a[i]==c[j]:
                print(b[j])
                break

main()

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.append(K+1)
    for i in range(N):
        print((K-a[i]+1)//N)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    num = k//n
    res = [num]*n
    k = k%n
    for i in range(k):
        res[i] += 1
    for i in range(n):
        print(res[a.index(i+1)])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    num = k // n
    mod = k % n
    for i in range(n):
        if i < mod:
            print(num + 1)
        else:
            print(num)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    cnt = k//n
    rem = k%n
    for i in range(n):
        if i < rem:
            print(cnt+1)
        else:
            print(cnt)

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    ans = [k//n for i in range(n)]
    k = k%n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[a.index(a[i])])

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*n
    for i in range(n):
        b[i] = k//n
    for i in range(k%n):
        b[i] += 1
    for i in range(n):
        print(b[a.index(a[i])])

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 从小到大排序
    a.sort()
    # 每个人最少拿一个
    k = k - n
    # 每个人拿的个数
    num = k // n
    # 拿不完的人数
    num2 = k % n
    # 拿不完的人的id
    id = a[num2]
    # 拿完的人拿的个数
    num3 = num + 1
    # 拿完的人的id
    id2 = id - 1
    # 输出
    for i in range(n):
        if a[i] <= id:
            print(num3)
        else:
            print(num)
