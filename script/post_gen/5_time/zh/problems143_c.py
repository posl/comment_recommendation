Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    s_list = list(s)
    s_list.a

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    S = list(S)
    i = 0
    while i < len(S)-1:
        if S[i] == S[i+1]:
            del S[i+1]
            i -= 1
        else:
            i += 1
    print(len(S))

=======
Suggestion 4

def solve():
    N = int(input())
    S = input()
    s = S[0]
    count = 1
    for i in range(1,N):
        if s != S[i]:
            s = S[i]
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def merge_slimes(slimes):
    merged_slimes = []
    prev_slime = None
    for slime in slimes:
        if prev_slime is None:
            prev_slime = slime
        elif prev_slime == slime:
            pass
        else:
            merged_slimes.append(prev_slime)
            prev_slime = slime
    merged_slimes.append(prev_slime)
    return merged_slimes

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    s = list(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s.pop(i)
        else:
            i += 1
    print(len(s))

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(1,N):
        if S[i] != S[i-1]:
            count += 1
    print(count)

=======
Suggestion 9

def count_slime(s):
    count = 1
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            count += 1
    return count
