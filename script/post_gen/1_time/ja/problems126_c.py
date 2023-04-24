Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        cnt = 0
        while i < K:
            i *= 2
            cnt += 1
        ans += (1/N) * (0.5)**cnt
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        p = 1/n
        x = i
        while x < k:
            x *= 2
            p /= 2
        ans += p
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
        else:
            cnt = 0
            while i < K:
                i *= 2
                cnt += 1
            ans += (1/N) * (1/2)**cnt
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1
            continue
        cnt = 0
        tmp = i
        while tmp < K:
            tmp *= 2
            cnt += 1
        ans += (1/N) * (1/2)**cnt
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    p = 0
    for i in range(1, N+1):
        if i >= K:
            p += 1
            continue
        j = i
        while j < K:
            j *= 2
            p += 1
    print(p/(N*2**(p-1)))

=======
Suggestion 6

def main():
    import math
    N, K = map(int, input().split())
    if K == 1:
        print(1)
        return
    ans = 0
    for i in range(1, N+1):
        x = i
        cnt = 0
        while x < K:
            x *= 2
            cnt += 1
        ans += 1/N * (1/2)**cnt
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
        return
    if N == 1:
        print(1)
        return
    if N == 2:
        print(1/2)
        return
    if N == 3:
        print(1/3)
        return
    if N == 4:
        print(1/4)
        return
    if N == 5:
        print(1/5)
        return
    if N == 6:
        print(1/6)
        return
    if N == 7:
        print(1/7)
        return
    if N == 8:
        print(1/8)
        return
    if N == 9:
        print(1/9)
        return
    if N == 10:
        print(1/10)
        return
    if N == 11:
        print(1/11)
        return
    if N == 12:
        print(1/12)
        return
    if N == 13:
        print(1/13)
        return
    if N == 14:
        print(1/14)
        return
    if N == 15:
        print(1/15)
        return
    if N == 16:
        print(1/16)
        return
    if N == 17:
        print(1/17)
        return
    if N == 18:
        print(1/18)
        return
    if N == 19:
        print(1/19)
        return
    if N == 20:
        print(1/20)
        return
    if N == 21:
        print(1/21)
        return
    if N == 22:
        print(1/22)
        return
    if N == 23:
        print(1/23)
        return
    if N == 24:
        print(1/24)
        return
    if N == 25:
        print(1/25)
        return
    if N == 26:
        print(1/26)
        return
    if N == 27:
        print(1/27)
        return
    if N == 28:
        print(1/28)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    if N < K:
        print(0)
        return
    ans = 0
    for i in range(1, N+1):
        if i >= K:
            ans += 1/N
            continue
        else:
            ans += 1/(N*(2**((K-i-1).bit_length())))
    print(ans)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    # 1回目のサイコロ
    ans = 0
    # 2回目以降のサイコロ
    for i in range(1, N+1):
        # 1回目のサイコロでK以上になる確率
        if i >= K:
            ans += 1/N
        # 2回目以降のサイコロでK以上になる確率
        else:
            # 1回目のサイコロの出目
            tmp = i
            # 2回目以降のサイコロの出目
            j = 1
            while tmp < K:
                tmp *= 2
                j += 1
            ans += 1/N * (1/2)**(j-1)
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    # N = 6, K = 5
    # 1 2 3 4 5 6
    # 1 2 3 4 5
    # 1 2 3 4
    # 1 2 3
    # 1 2
    # 1
    # 1/6 * 1/2 * (1/2)^4
    # 1/6 * 1/2 * (1/2)^3
    # 1/6 * 1/2 * (1/2)^2
    # 1/6 * 1/2 * (1/2)^1
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0
    # 1/6 * 1/2 * (1/2)^0

    # 1/6 * 1/2 * (1/2)^4 + 1/6 * 1/2 * (1/2)^3 + 1/
