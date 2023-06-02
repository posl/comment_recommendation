Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))

    # 一直往右走，直到到达最右边
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i] += 1

    print(H[-1])

=======
Suggestion 2

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    print(max_h)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    h.reverse()
    ans = 0
    now = 0
    for i in range(n):
        if now < h[i]:
            ans += 1
            now = h[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if i == N - 1:
            ans = H[i]
        elif H[i] < H[i+1]:
            ans = H[i+1]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n):
        if max_h <= h[i]:
            max_h = h[i]
    print(max_h)

=======
Suggestion 6

def get_input():
    N = int(input())
    H = list(map(int, input().split()))
    return N, H

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    for i in range(n):
        if h[i] >= max:
            max = h[i]
    print(max)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))

    max = 0
    for i in range(N):
        if max <= H[i]:
            max = H[i]

    print(max)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            max_h = h[i+1]
    print(max_h)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))

    # 从左向右遍历，如果后一个比前一个大，那么就上去
    # 如果后一个比前一个小，那么就停止
    # 一直到最后一个
    # 所以就是找到最大的那个
    max_h = 0
    for i in range(n):
        if max_h < h[i]:
            max_h = h[i]

    print(max_h)
