Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    max_count = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

=======
Suggestion 2

def main():
    n=int(input())
    h_list=list(map(int,input().split()))
    count=0
    for i in range(1,n):
        if h_list[i-1]>=h_list[i]:
            count+=1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    cnt = 0
    ans = 0
    for i in range(n):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
        else:
            ans = max(ans,cnt)
            cnt = 0
    ans = max(ans,cnt)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    H = [int(x) for x in input().split()]

    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i] <= h[i - 1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i] <= h[i - 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(max_count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    tmp = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            tmp += 1
        else:
            tmp = 0
        if tmp > count:
            count = tmp
    print(count)

=======
Suggestion 10

def solve():
    # 从左向右遍历, 用一个变量来记录当前的最大值
    # 从左向右遍历, 如果当前值小于等于最大值, 则计数+1, 并将最大值更新为当前值
    # 如果当前值大于最大值, 则计数清零, 并将最大值更新为当前值
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            count += 1
            max_h = h[i]
    print(count)
    return 0
