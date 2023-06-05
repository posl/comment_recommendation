Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
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
Suggestion 2

def max_move(n, h):
    max_move = 0
    for i in range(0, n):
        move = 1
        for j in range(i, n-1):
            if h[j] <= h[j+1]:
                move += 1
            else:
                break
        if move > max_move:
            max_move = move
    return max_move

=======
Suggestion 3

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
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
    H = [int(x) for x in input().split()]
    count = 0
    max_count = 0
    for i in range(n-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int,input().split()))
    ans = 0
    cnt = 0
    for i in range(1,n):
        if h[i-1] >= h[i]:
            cnt += 1
        else:
            ans = max(ans,cnt)
            cnt = 0
    ans = max(ans,cnt)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(h[i])
        if i > 0 and h[i] <= h[i-1]:
            l.append(0)
    print(max(l))

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 8

def solve():
    n = int(input())
    height = list(map(int, input().split()))
    max_height = 0
    count = 0
    for i in range(n):
        if height[i] >= max_height:
            max_height = height[i]
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    count = 1
    max_count = 1
    for i in range(1, n):
        if h[i-1] >= h[i]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1
    if max_count < count:
        max_count = count
    print(max_count-1)
