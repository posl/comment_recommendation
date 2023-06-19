Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 一开始的镇
    start = 1

    # 从第一次开始循环
    for i in range(k):
        start = a[start - 1]

    # 输出结果
    print(start)

=======
Suggestion 2

def main():
    N,K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    count = 0
    i = 0
    while count < K:
        count += 1
        i = A[i] - 1
        if i == 0:
            break
    print(A[i])

=======
Suggestion 3

def solve(n, k, a):
    k = k % n
    for i in range(k):
        a = a[a-1]
    return a

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    i = 0
    while k > 0:
        i = a[i] - 1
        k -= 1
    print(i+1)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    K = K % N
    for i in range(K):
        A = list(map(lambda x: A[x - 1], A))
    print(A[0])

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,k,a)
    #print(a)
    for i in range(k):
        a = a[a[i]-1:] + a[:a[i]-1]
        #print(a)
    print(a[0])

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    b[0] = 1
    c = 0
    for i in range(1, n+1):
        c = a[c] - 1
        if b[c] > 0:
            break
        else:
            b[c] = i + 1
    if i == n:
        print(c+1)
    else:
        d = i - b[c] + 1
        e = (k - i) % d
        for i in range(e):
            c = a[c] - 1
        print(c+1)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 1
    for i in range(1, n):
        b[i] = a[b[i-1]-1]
    if k <= n:
        print(b[k-1])
        return
    k = (k - n) % (n - b.index(b[n-1]))
    print(b.index(b[n-1] + k) + 1)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    now = 0
    for i in range(60, -1, -1):
        if k & (1 << i):
            now = a[now]
            for j in range(i):
                now = a[now]
    print(now + 1)

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    town = 1
    for i in range(K):
        town = A[town-1]
    print(town)
