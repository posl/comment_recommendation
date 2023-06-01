Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if h[i] >= k:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def get_input():
    # input
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    return n,k,h

=======
Suggestion 3

def fun1():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 4

def count_roller_coaster(N, K, h):
    count = 0
    for i in range(N):
        if h[i] >= K:
            count += 1
    return count

=======
Suggestion 5

def check_ride_roller_coaster(n,k,h):
    count=0
    for i in h:
        if i>=k:
            count+=1
    return count

=======
Suggestion 6

def solve(n,k,h):
    ans = 0
    for i in range(n):
        if h[i] >= k:
            ans += 1
    return ans

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= k:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    # 读取输入
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    # 初始化
    ans = 0
    # 遍历
    for i in h:
        if i >= k:
            ans += 1
    # 输出结果
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in h:
        if i >= K:
            count += 1
    print(count)
