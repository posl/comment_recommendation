Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] >= K:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in range(0,n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in h:
        if i >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    n,k = map(int,input().split())
    h = list(map(int,input().split()))

    # 遍历数据
    count = 0
    for i in h:
        if i >= k:
            count += 1
    
    # 打印结果
    print(count)
