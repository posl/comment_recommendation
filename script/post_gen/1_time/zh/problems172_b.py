Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
main()

=======
Suggestion 5

def solve(s,t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print(0)
        return
    else:
        count = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                count += 1
        print(count)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i + j < n:
                if s[i + j] != t[j]:
                    cnt += 1
            else:
                if s[i + j - n] != t[j]:
                    cnt += 1
        ans = min(ans, cnt)
    print(ans)
