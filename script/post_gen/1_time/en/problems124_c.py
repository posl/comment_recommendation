Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == '1':
                count += 1
        else:
            if s[i] == '0':
                count += 1
    print(count)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '1':
                count += 1
        else:
            if S[i] == '0':
                count += 1
    print(count)

=======
Suggestion 3

def solve():
    S = input()
    count = 0
    for i in range(len(S)):
        if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == '0':
                count += 1
        else:
            if S[i] == '1':
                count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    if len(s) == 1:
        print(0)
    else:
        count = 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
        print(count)

=======
Suggestion 6

def main():
    S = input().strip()
    count = 0
    for i in range(0,len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    S = input()
    count = 0
    if S == "0" or S == "1":
        print(count)
    else:
        for i in range(len(S)):
            if i == 0:
                if S[i] == "0":
                    count += 1
            else:
                if S[i] != S[i-1]:
                    count += 1
        print(count)

=======
Suggestion 8

def solve():
    s = input()
    n = len(s)
    a = 0
    for i in range(n):
        if int(s[i]) == (i % 2):
            a += 1
    print(min(a, n - a))
