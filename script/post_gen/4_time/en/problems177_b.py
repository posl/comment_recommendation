Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    ans = 1000
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
    S = input()
    T = input()
    count = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 7

def solve():
    S = input()
    T = input()
    min = len(T)
    for i in range(len(S) - len(T) + 1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 8

def main():
    S = input()
    T = input()

    min_change = len(T)
    for i in range(len(S) - len(T) + 1):
        change = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                change += 1
        if change < min_change:
            min_change = change

    print(min_change)

=======
Suggestion 9

def solve():
    s = input()
    t = input()
    res = len(t)
    for i in range(len(s) - len(t) + 1):
        c = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                c += 1
        res = min(res, c)
    print(res)

=======
Suggestion 10

def problem():
    s = input()
    t = input()
    min = len(t)
    for i in range(0, len(s)-len(t)+1):
        count = 0
        for j in range(0, len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

problem()
