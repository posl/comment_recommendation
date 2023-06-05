Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a') + 1)

=======
Suggestion 2

def solve():
    s = input()
    ans = -1
    for i in range(len(s)):
        if s[i] == 'a':
            ans = i + 1
    print(ans)

solve()

=======
Suggestion 3

def main():
    S = input()
    if 'a' in S:
        print(S.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 4

def find_last(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index

s = input()
c = 'a'
print(find_last(s, c))

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 6

def main():
    s = input()
    print(s.rfind("a") + 1)

=======
Suggestion 7

def find_last_index(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index

=======
Suggestion 8

def last_index(s, c):
    return s.rfind(c)

=======
Suggestion 9

def main():
    S = input()
    print(S.rfind('a')+1)
