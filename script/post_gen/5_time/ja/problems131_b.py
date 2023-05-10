Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    min

=======
Suggestion 2

def main():
    n, l = map(int, input().split())
    li = [l+i for i in range(n)]
    print(sum(li[1:]) - li[0])

=======
Suggestion 3

def solve(n, l):
    return sum(l) - min(l, key=abs)*2

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    ans = 0
    minv = 10000
    for i in range(0, N):
        tmp = L + i
        if(abs(tmp) < minv):
            minv = abs(tmp)
            ans = tmp
    print((N-1)*N//2 + ans)

=======
Suggestion 5

def main():
    n, l = map(int, input().split())
    sum = 0
    min = 10000000
    for i in range(n):
        sum += l + i
        if min > abs(l + i):
            min = abs(l + i)
    print(sum - min)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    total = 0
    min_diff = 10**10
    for i in range(N):
        total += L + i
        if abs(L + i) < abs(min_diff):
            min_diff = L + i
    print(total - min_diff)

=======
Suggestion 7

def solve():
    N, L = map(int, input().split())
    total = 0
    for i in range(N):
        total += L + i
    if L >= 0:
        print(total - L - N)
    elif L + N - 1 <= 0:
        print(total - L)
    else:
        print(total)

=======
Suggestion 8

def main():
    N, L = map(int, input().split())
    if L >= 0:
        print((L + N - 1) * (L + N) // 2 - L)
    elif L < 0 and L + N - 1 >= 0:
        print((L + N - 1) * (L + N) // 2)
    else:
        print((L + N - 1) * (L + N) // 2 - (L + N - 1))

=======
Suggestion 9

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    n,l = map(int, input().split())
    sum = 0
    min = 1000
    for i in range(n):
        sum += l + i
        if abs(l+i) < min:
            min = abs(l+i)
    if l >= 0:
        sum -= min
    elif l < 0 and l+n-1 > 0:
        sum += min
    else:
        sum -= min
    print(sum)

=======
Suggestion 10

def main():
    n, l = map(int, input().split())
    taste = [l+i for i in range(n)]
    min_index = taste.index(min(taste, key=abs))
    print(sum(taste[:min_index]+taste[min_index+1:]))
