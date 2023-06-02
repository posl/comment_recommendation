Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    count = 0
    #先把白色石头移到最右边
    for i in range(N):
        if c[i] == 'W':
            count += 1
    print(count)
    return 0

=======
Suggestion 2

def main():
    #读入数据
    n = int(input())
    c = input()
    #统计白色石头的数量
    w = c.count('W')
    #统计白色石头的数量
    r = c.count('R')
    #如果白色石头的数量大于0，则可以进行操作
    if w > 0:
        #从左边开始，统计白色石头的数量
        w_left = c[:w].count('W')
        #从右边开始，统计红色石头的数量
        r_right = c[w:].count('R')
        #打印结果
        print(min(w_left, r_right))
    else:
        #如果白色石头的数量为0，则不需要操作
        print(0)

=======
Suggestion 3

def get_min_op_num(stones):
    white_stone_num = stones.count('W')
    if white_stone_num == 0:
        return 0
    else:
        white_stone_idx = stones.index('W')
        red_stone_idx = stones.rindex('R')
        red_stone_num = stones.count('R')
        if red_stone_idx < white_stone_idx:
            return white_stone_num
        else:
            return red_stone_num - white_stone_num

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def main():
    N = int(input())
    c = list(input())
    R = c.count('R')
    W = c.count('W')
    if R == 0 or W == 0:
        print(0)
    else:
        r = 0
        w = 0
        for i in range(R):
            if c[i] == 'W':
                r += 1
        for i in range(R, N):
            if c[i] == 'R':
                w += 1
        print(min(r, w))

=======
Suggestion 6

def solve(N, cs):
    ans = 0
    for i in range(N):
        if cs[i] == "W":
            ans += 1
    if ans == 0:
        return 0
    elif ans == N:
        return N
    else:
        r = 0
        w = ans
        for i in range(N):
            if cs[i] == "R":
                r += 1
            else:
                w -= 1
            ans = min(ans, max(r, w))
        return ans

=======
Suggestion 7

def main():
    N = int(input())
    c = input()
    left = 0
    right = N - 1
    ans = 0
    while True:
        while left < N and c[left] == 'R':
            left += 1
        while right >= 0 and c[right] == 'W':
            right -= 1
        if left >= right:
            break
        ans += 1
        left += 1
        right -= 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    print(w)

=======
Suggestion 9

def main():
    n = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(n):
        if c[i] == 'R':
            r += 1
        else:
            w += 1
    ans = min(r,w)
    for i in range(ans):
        if c[i] == 'W':
            ans -= 1
    print(ans)

=======
Suggestion 10

def min_swap(s):
    n = len(s)
    r = 0
    w = 0
    for i in range(n):
        if s[i] == 'R':
            r += 1
        else:
            w += 1
    if r == 0 or w == 0:
        return 0
    if s[0] == 'R':
        r -= 1
    else:
        w -= 1
    if s[-1] == 'R':
        r -= 1
    else:
        w -= 1
    return min(r, w) + 1
