Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L = map(int, input().split())
    print(sum(range(L + N - 1, L - 1, -1)) - min(range(L + N - 1, L - 1, -1), key=abs))

=======
Suggestion 2

def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += l + i
    if l > 0:
        ans -= l
    elif l + n - 1 < 0:
        ans -= l + n - 1
    print(ans)

=======
Suggestion 3

def main():
    N, L = map(int, input().split())
    sum = 0
    for i in range(1, N+1):
        sum += L + i - 1
    if L >= 0:
        print(sum - L - 1)
    elif L + N - 1 < 0:
        print(sum - L - N)
    else:
        print(sum)

=======
Suggestion 4

def main():
    n, l = map(int, input().split())
    ans = 0
    if l >= 0:
        ans = (l + n - 1) * (l + n) // 2 - l
    elif l + n - 1 < 0:
        ans = (l + n - 1) * (l + n) // 2 - l
    else:
        ans = (l + n - 1) * (l + n) // 2
    print(ans)

=======
Suggestion 5

def main():
    n,l = map(int,input().split())
    ans = 0
    if l >= 0:
        ans = sum(range(l+1,l+n))
    elif l+n-1 < 0:
        ans = sum(range(l,l+n-1))
    else:
        ans = sum(range(l+1,l+n))
    print(ans)

=======
Suggestion 6

def main():
    N, L = map(int, input().split())
    if L >= 0:
        print(sum(list(range(L+1, L+N))))
    elif L+N <= 0:
        print(sum(list(range(L+N, L))))
    else:
        print(sum(list(range(L, L+N))))

=======
Suggestion 7

def main():
    n, l = map(int, input().split())
    ans = 0
    min_diff = 10**9
    for i in range(n):
        taste = l+i
        ans += taste
        if abs(taste) < min_diff:
            min_diff = abs(taste)
            min_taste = taste
    print(ans-min_taste)

=======
Suggestion 8

def cal(n, l):
    sum = 0
    for i in range(1,n+1):
        sum += l + i - 1
    return sum

n, l = map(int, input().split())

=======
Suggestion 9

def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    N, L = map(int, input().split())
    # print(N, L)
    sum = 0
    min = 10000
    for i in range(N):
        sum += L + i
        if abs(L + i) < min:
            min = abs(L + i)
    # print(sum, min)
    if L >= 0:
        print(sum - min)
    elif L + N - 1 <= 0:
        print(sum - (L + N - 1))
    else:
        print(sum)

=======
Suggestion 10

def calc_apple_pie_score(n, l, i):
    total = 0
    for j in range(n):
        if j != i:
            total += l + j
    return total
