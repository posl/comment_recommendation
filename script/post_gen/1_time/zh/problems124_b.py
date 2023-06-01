Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = input()
    h = input()
    return n, h

=======
Suggestion 2

def problems124_b():
    n = int(input())
    h = list(map(int,input().split()))
    max_h = 0
    count = 0
    for i in range(n):
        if max_h <= h[i]:
            max_h = h[i]
            count += 1
    print(count)

=======
Suggestion 3

def get_see_count():
    N = int(input())
    H = list(map(int, input().split()))
    see_count = 0
    for i in range(N):
        see = True
        for j in range(i):
            if H[i] < H[j]:
                see = False
                break
        if see:
            see_count += 1
    print(see_count)

=======
Suggestion 4

def main():
    N = int(input())
    H_list = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            if max(H_list[:i]) <= H_list[i]:
                count += 1
    print(count)

=======
Suggestion 5

def find_sea(h):
    cnt = 1
    max_h = h[0]
    for i in range(1, len(h)):
        if h[i] > max_h:
            cnt += 1
            max_h = h[i]
    return cnt

=======
Suggestion 6

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        if nums[i-1] <= nums[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[i] < H[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        flag = True
        for j in range(i):
            if H[j] >= H[i]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        flag = True
        for j in range(0, i):
            if H[j] >= H[i]:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    # print(n, h)
    count = 0
    for i in range(n):
        flag = True
        for j in range(i):
            if h[i] < h[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)
