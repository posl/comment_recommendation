Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solution(S):
    return S.rfind("a")+1

=======
Suggestion 2

def main():
    S = input()
    print(S.rfind('a')+1)

=======
Suggestion 3

def solve():
    #在这里编写你的代码
    S = input()
    index = -1
    for i in range(len(S)):
        if S[i] == 'a':
            index = i + 1
    print(index)

=======
Suggestion 4

def main():
    S = input()
    # 请在此添加代码
    print(S.rfind("a")+1)

=======
Suggestion 5

def last_index_of_a(s):
    index = -1
    for i, c in enumerate(s):
        if c == 'a':
            index = i + 1
    return index

=======
Suggestion 6

def solve():
    S = input()
    if 'a' in S:
        print(S.rfind('a')+1)
    else:
        print(-1)

=======
Suggestion 7

def lastIndex(s):
    #请在这里编写代码
    if s.rfind('a') == -1:
        print(-1)
    else:
        print(s.rfind('a')+1)

=======
Suggestion 8

def main():
    s = input()
    print(s.rfind('a') + 1 if s.rfind('a') != -1 else -1)
