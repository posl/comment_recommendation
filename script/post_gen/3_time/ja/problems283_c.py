Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            ans += 1
        else:
            ans += 2
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != '0':
            ans += 1
    ans += len(S) - 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == '0':
            ans += 1
        else:
            ans += 2
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    ans = 0
    for i in range(len(S)):
        if i == 0:
            ans += int(S[i])
        else:
            if int(S[i]) == 0:
                ans += 1
            else:
                ans += int(S[i]) + 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i] != '0':
            ans += int(s[i]) - 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += int(S[i])
        else:
            if S[i] != '0':
                ans += int(S[i]) + 1
            else:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    for i in range(1, len(s)):
        ans += 10
    ans += int(s[0]) + len(s) - 1
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '0':
            pass
        else:
            ans += 1
    if S[0] != '1':
        ans += len(S) - 1
    else:
        ans += len(S) - 2
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    print(len(S))
