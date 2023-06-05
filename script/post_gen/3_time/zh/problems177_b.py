Synthesizing 10/10 solutions

=======
Suggestion 1

def problem177b(s, t):
    # S, T = input().split()
    # s = 'cabacc'
    # t = 'abc'
    # print(s, t)
    # print(len(s), len(t))
    # print(s[3], t[1])
    # print(s[2:5], t)
    # print(s[2:5] == t)
    # print(s[2] == t[0])
    # print(s[3] == t[1])
    # print(s[4] == t[2])
    # print(s[2] == t[0]

=======
Suggestion 2

def diff(s, t):
    n = len(s)
    m = len(t)
    ans = n
    for i in range(n-m+1):
        tmp = 0
        for j in range(m):
            if s[i+j] != t[j]:
                tmp += 1
        ans = min(ans, tmp)
    return ans

=======
Suggestion 3

def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    n = len(S)
    m = len(T)
    ans = 1000
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

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

solve()

=======
Suggestion 5

def main():
    S = input()
    T = input()
    #print(S,T)
    count = 0
    i = 0
    while i < len(S):
        if S[i] != T[i]:
            count += 1
        i += 1
    print(count)

=======
Suggestion 6

def main():
    s = input()
    t = input()
    #print(s,t)
    count = 0
    for i in range(len(s)-len(t)+1):
        #print(i)
        #print(s[i:i+len(t)])
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
    print(count)
main()

=======
Suggestion 7

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = m
    for i in range(n - m + 1):
        cnt = 0
        for j in range(m):
            if s[i + j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def solve():
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

solve()

=======
Suggestion 9

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    # print(S_len)
    # print(T_len)
    min = 1000
    for i in range(S_len-T_len+1):
        # print(i)
        # print(S[i:i+T_len])
        count = 0
        for j in range(T_len):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 10

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
