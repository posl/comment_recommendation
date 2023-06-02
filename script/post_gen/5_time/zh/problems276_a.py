Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 2

def last_index(s, c):
    return s.rfind(c) + 1

s = input()
c = 'a'
print(last_index(s, c))

=======
Suggestion 3

def main():
    # 请在下面编写你的代码
    s = input()
    print(s.rfind('a')+1)

=======
Suggestion 4

def main():
    s = input()
    if s.count('a') == 0:
        print(-1)
    else:
        print(s.rfind('a') + 1)

=======
Suggestion 5

def problem276_a():
    S = input()
    if 'a' in S:
        print(S.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 7

def last_index(s):
    index = -1
    for i in range(len(s)):
        if s[i] == "a":
            index = i
    return index + 1

=======
Suggestion 8

def get_last_index(s, c):
    index = -1
    for i in range(len(s)):
        if s[i] == c:
            index = i + 1
    return index

=======
Suggestion 9

def main():
    S = input()
    n = len(S)
    for i in range(n-1,-1,-1):
        if S[i] == 'a':
            print(i+1)
            exit()
    print(-1)
