Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    h = list(map(int, input().split()))
    return n, h

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 3

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    maxh = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            maxh = h[i+1]
    print(maxh)

=======
Suggestion 4

def main():
    # 读取输入
    n = int(input())
    h = list(map(int, input().split()))

    # 从左到右，找到最后一个比左边高的平台
    ans = 0
    for i in range(n - 1):
        if h[i] < h[i + 1]:
            ans = h[i + 1]

    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    res = h[0]
    for i in range(1, n):
        if h[i] > h[i-1]:
            res = h[i]
    print(res)

=======
Suggestion 6

def main():
    num = int(input())
    height = list(map(int, input().split()))
    max_height = 0
    for i in range(num):
        if height[i] > max_height:
            max_height = height[i]
    print(max_height)

=======
Suggestion 7

def main():
    n = int(input())
    H = list(map(int, input().split()))
    max_height = 0
    for i in range(n):
        if H[i] >= max_height:
            max_height = H[i]
    print(max_height)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    ans = 0
    for i in range(n):
        if h[i] < h[i + 1]:
            ans = h[i + 1]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))

    # 从左边开始，找到最大的那个，然后从右边开始，找到最大的那个，然后比较两个最大的那个，取最大的那个
    # 从左边开始，找到最大的那个
    max_left = 0
    for i in range(n):
        if h[i] > max_left:
            max_left = h[i]
    # 从右边开始，找到最大的那个
    max_right = 0
    for i in range(n-1, -1, -1):
        if h[i] > max_right:
            max_right = h[i]
    # 比较两个最大的那个，取最大的那个
    if max_right > max_left:
        print(max_right)
    else:
        print(max_left)

=======
Suggestion 10

def findLastPlatform(heights):
    lastPlatform = heights[0]
    for i in range(1, len(heights)):
        if heights[i] > lastPlatform:
            lastPlatform = heights[i]
    return lastPlatform
