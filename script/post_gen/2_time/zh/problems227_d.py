Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N-1):
        B.append(A[i+1]-A[i])
    B.sort()
    ans = sum(B[:N-K])
    print(ans)

=======
Suggestion 2

def main():
    # 读取输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort() # 排序
    # print(n, k, a)
    # 统计每个部门的人数
    count = 1
    num = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            count += 1
        else:
            num += count // k
            count = 1
    num += count // k
    print(num)

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - k + 1):
        ans += a[i]
    print(ans)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k >= n:
        print(0)
        exit()
    else:
        print(a[k-1])

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    print(n,k)
    print(a[0:k])
    print(a[n-k:n])
    print(max(a[0:k])+max(a[n-k:n]))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    print(a)
    print(a[n-k])
    print(a[n-1])
    if a[n-k] == a[n-1]:
        print(n)
    else:
        print(n-k)

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-k+1):
        if (a[i+k-1] - a[i]) < ans or ans == 0:
            ans = a[i+k-1] - a[i]
    print(ans)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n-k):
        count += a[i]
    print(count)
