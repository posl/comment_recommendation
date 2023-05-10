Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                count += 1
        ans = min(ans, count)
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if t[j] != s[i+j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    count = 1000
    for i in range(len(s)-len(t)+1):
        tmp = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                tmp += 1
        count = min(tmp, count)
    print(count)

=======
Suggestion 4

def solve():
    s = input()
    t = input()
    ans = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    slen = len(s)
    tlen = len(t)
    ans = tlen
    for i in range(slen-tlen+1):
        cnt = 0
        for j in range(tlen):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

main()  # 出力結果 0.0sec

=======
Suggestion 6

def main():
    s = input()
    t = input()
    ans = len(t)
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                count += 1
        ans = min(ans, count)
    print(ans)

=======
Suggestion 7

def solve(s,t):
    min = len(t)
    for i in range(len(s)-len(t)+1):
        cnt = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                cnt += 1
        if cnt < min:
            min = cnt
    return min

=======
Suggestion 8

def solve():
    S = input()
    T = input()
    min = len(T)
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        if min > tmp:
            min = tmp
    print(min)

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        cnt = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 10

def main():
    s = input()
    t = input()
    ans = 1000
    for i in range(len(s) - len(t) + 1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        ans = min(ans, count)
    print(ans)
