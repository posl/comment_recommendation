Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = n
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            if s[i+j] != t[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    ans = 1000
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        ans = min(ans,tmp)
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    count = 0
    for i in range(S_len-T_len+1):
        for j in range(T_len):
            if S[i+j] != T[j]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    min = len_t
    for i in range(len_s-len_t+1):
        cnt = 0
        for j in range(len_t):
            if s[i+j] != t[j]:
                cnt += 1
        if cnt < min:
            min = cnt
    print(min)

=======
Suggestion 6

def main():
    S = input()
    T = input()

    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(t)):
        ans += 1 if t[i] != s[i] else 0
    print(ans)

main()

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S = list(S)
    T = list(T)
    S.reverse()
    T.reverse()
    ans = 0
    for i in range(len(T)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    s = input()
    t = input()
    print(len(t) - max([len([1 for i in range(len(t)) if s[i+j] == t[i]]) for j in range(len(s)-len(t)+1)]))

=======
Suggestion 10

def main():
    S = input()
    T = input()
    #print(S,T)
    print(len(T) - max([len([1 for j in range(len(T)) if S[i+j] == T[j]]) for i in range(len(S)-len(T)+1)]))
