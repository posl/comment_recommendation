Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)

=======
Suggestion 2

def solve():
    N = int(input())
    H = list(map(int, input().split()))
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
Suggestion 3

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

=======
Suggestion 4

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max_cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
    max_cnt = max(max_cnt, cnt)
    print(max_cnt)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    print(max_count)

=======
Suggestion 6

def main():
    n = int(input())
    heights = list(map(int, input().split()))

    count = 0
    max_count = 0
    for i in range(n-1):
        if heights[i] >= heights[i+1]:
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
    h = [int(i) for i in input().split()]

    count = 0
    max_count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    print(max_count)

=======
Suggestion 8

def max_move(n, h):
    max_move = 0
    current_move = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            current_move += 1
        else:
            current_move = 0
        if current_move > max_move:
            max_move = current_move
    return max_move

n = int(input())
h = list(map(int, input().split()))
print(max_move(n, h))

=======
Suggestion 9

def max_move(n, heights):
    max_count = 0
    count = 0
    for i in range(n-1):
        if heights[i] >= heights[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count

=======
Suggestion 10

def main():
    num = int(input())
    height = list(map(int, input().split()))
    max_num = 0
    count = 0
    for i in range(1,num):
        if height[i-1] >= height[i]:
            count += 1
        else:
            count = 0
        if max_num < count:
            max_num = count
    print(max_num)
