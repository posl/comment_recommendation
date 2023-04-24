Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    if len(S) == 1:
        print(0)
        return
    ans = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    prev = S[0]
    count = 0
    for i in range(1,len(S)):
        if S[i] == prev:
            count += 1
        else:
            prev = S[i]
    print(count)

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        exit()
    ans = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    #print(S)
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 9

def get_input():
    return input()
