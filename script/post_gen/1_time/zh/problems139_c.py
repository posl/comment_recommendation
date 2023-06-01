Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))

    cnt = 0
    max_cnt = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    print(max_cnt)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(1, n):
        if h[i] <= h[i-1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    print(max_count)

=======
Suggestion 3

def solve():
    N = int(input())
    H = list(map(int, input().split()))

    cnt = 0
    ans = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    res = 0
    cnt = 0
    for i in range(n):
        if i == 0:
            res = h[i]
            cnt += 1
        else:
            if res <= h[i]:
                cnt += 1
                res = h[i]
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 6

def get_max_height_index(height_list):
    max_height = 0
    max_height_index = 0
    for i in range(len(height_list)):
        if height_list[i] > max_height:
            max_height = height_list[i]
            max_height_index = i
    return max_height_index

=======
Suggestion 7

def main():
    #输入
    n = int(input())
    h = list(map(int, input().split()))

    #计算
    max_move = 0
    move = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            move += 1
        else:
            move = 0
        if move > max_move:
            max_move = move

    #输出
    print(max_move)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    # print(n)
    # print(h)
    max = 0
    count = 0
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    print(max)

=======
Suggestion 9

def solve(n, h):
    ans = 0
    cnt = 0
    for i in range(1, n):
        if h[i] <= h[i - 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    return ans

n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int,input().split()))
    count = 0
    max_count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)
