Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    ans = 0
    for i in range(N-1):
        if c[i] == 'R' and c[i+1] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    C = input()
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        exit()
    r = 0
    w = 0
    ans = 1000000000
    for i in range(N):
        if C[i] == 'R':
            r += 1
        else:
            w += 1
        ans = min(ans, r + W - w)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    s = input()
    R = [0 for i in range(N)]
    W = [0 for i in range(N)]
    for i in range(N):
        if s[i] == "R":
            R[i] = 1
        else:
            W[i] = 1
    for i in range(N-1):
        R[i+1] += R[i]
        W[i+1] += W[i]
    ans = N
    for i in range(N):
        ans = min(ans, i+1-R[i]+W[N-1]-W[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    s = input()

    ans = 0
    r = 0
    for i in range(N):
        if s[i] == 'R':
            r += 1
        else:
            ans += r

    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    c = input()
    cnt = 0
    for i in range(n):
        if c[i] == 'R':
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    ans = 0
    if s[0] == 'W':
        ans += 1
    for i in range(n - 1):
        if s[i] == 'R' and s[i + 1] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == "R":
            count += 1
    print(min(count, N - count))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    count = 0
    for i in range(n):
        if s[i] == "R":
            count += 1
    print(min(count, n - count))

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    c = s.count('R')
    ans = s[:c].count('W')
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = list(input())
    # 白い石の数
    white = S.count('W')
    # 赤い石の数
    red = N - white
    # 赤い石が左側にある場合
    left_red = 0
    # 赤い石が右側にある場合
    right_red = red
    # 赤い石が左側にある場合の最小操作回数
    left_min = 0
    # 赤い石が右側にある場合の最小操作回数
    right_min = 0
    for i in range(N):
        if S[i] == 'R':
            left_red += 1
            right_red -= 1
        else:
            left_min = max(left_min, left_red)
            right_min = max(right_min, right_red)
    print(min(left_min, right_min))
