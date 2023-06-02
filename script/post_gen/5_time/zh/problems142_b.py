Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)

=======
Suggestion 2

def solve(n, k, h):
    result = 0
    for i in range(0, n):
        if h[i] >= k:
            result += 1
    return result

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    print(ans)

=======
Suggestion 4

def problem142_b():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    c = 0
    for i in h:
        if i >= k:
            c += 1
    print(c)

=======
Suggestion 5

def main():
    # 读取输入
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    # 计算结果
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if H[i] >= K:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    count=0
    for i in range(len(h)):
        if h[i]>=k:
            count+=1
    print(count)
