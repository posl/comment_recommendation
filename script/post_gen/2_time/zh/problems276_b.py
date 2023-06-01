Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def last_index_of_a(s):
    index = -1
    for i in range(len(s)):
        if s[i] == 'a':
            index = i + 1
    return index

=======
Suggestion 2

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 3

def last_index_of_a(text):
    index = -1
    for i in range(len(text)):
        if text[i] == 'a':
            index = i + 1
    return index

=======
Suggestion 4

def solve():
    S = input()
    print(S.rfind('a') + 1)
    return 0

=======
Suggestion 5

def main():
    S = input()
    index = -1
    for i in range(len(S)):
        if S[i] == 'a':
            index = i + 1
    print(index)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    if s.find('a') == -1:
        print(-1)
    else:
        print(len(s) - s.find('a'))

=======
Suggestion 7

def get_index(s):
    index = -1
    for i in range(len(s)):
        if s[i] == 'a':
            index = i + 1
    return index

=======
Suggestion 8

def solve(input):
    # 在这里编写你的代码
    return -1

=======
Suggestion 9

def main():
    s = input()
    a = s.rfind('a')
    print(a+1 if a != -1 else -1)
