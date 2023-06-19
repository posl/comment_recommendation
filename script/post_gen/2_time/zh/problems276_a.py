Synthesizing 10/10 solutions

=======
Suggestion 1

def func(s):
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'a':
            return i+1
    return -1

=======
Suggestion 2

def get_input():
    return input()

=======
Suggestion 3

def main():
    s = input()
    if s.rfind('a') != -1:
        print(s.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 5

def main():
    s = input()
    if 'a' in s:
        print(s.rindex('a')+1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    S = input()
    print(S.rfind("a")+1)

=======
Suggestion 7

def main():
    s = input()
    print(s.rfind('a') + 1 if 'a' in s else -1)

=======
Suggestion 8

def main():
    S = input()
    # write code here
    if S.find('a') != -1:
        print(S.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 9

def solve():
    S = input()
    if 'a' in S:
        print(S.rindex('a') + 1)
    else:
        print(-1)

=======
Suggestion 10

def find_last_index(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index
