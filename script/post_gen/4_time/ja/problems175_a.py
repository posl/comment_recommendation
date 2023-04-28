Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == 'R':
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 2

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 3

def main():
    s = input()
    max = 0
    count = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 4

def problem175a():
    s = input()
    if s == 'RRR':
        print(3)
    elif s == 'RRS' or s == 'SRR':
        print(2)
    elif s == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    s = input()
    r = 0
    m = 0
    for i in range(3):
        if s[i] == "R":
            r += 1
            if r > m:
                m = r
        else:
            r = 0
    print(m)

=======
Suggestion 6

def main():
    s = input()
    max_rain = 0
    rain = 0
    for i in range(3):
        if s[i] == "R":
            rain += 1
        else:
            max_rain = max(max_rain, rain)
            rain = 0
    max_rain = max(max_rain, rain)
    print(max_rain)

=======
Suggestion 7

def main():
    s = input()
    r = 0
    c = 0
    for i in range(3):
        if s[i] == "R":
            c += 1
            if c > r:
                r = c
        else:
            c = 0
    print(r)

=======
Suggestion 8

def main():
    S = input()
    S = S.replace('S', '0')
    S = S.replace('R', '1')
    S = S.replace('01', '0,1')
    S = S.replace('10', '1,0')
    S = S.replace('00', '0,0')
    S = S.replace('11', '1,1')
    S = S.split(',')
    print(max(map(len, S)))

=======
Suggestion 9

def solve():
    # === 数値の入力 ===
    # N = int(input())
    # a, b = map(int, input().split())
    # A = list(map(int, input().split()))
    S = input()
    # ==================
    ans = 0
    cnt = 0
    for s in S:
        if s == "R":
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    r = s.count("R")
    print(r)
