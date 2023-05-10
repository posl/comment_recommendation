Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    S = input()
    if S.find('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 2

def main():
    s = str(input())
    if s.count("a") == 0:
        print(-1)
    else:
        print(s.rfind("a") + 1)

=======
Suggestion 3

def main():
    s = input()
    if s.count('a') == 0:
        print(-1)
    else:
        print(s.rfind('a') + 1)

=======
Suggestion 4

def main():
    s = input()
    if s.find('a') == -1:
        print(-1)
    else:
        print(s.rfind('a')+1)

=======
Suggestion 5

def main():
    S = input().rstrip()
    if S.count("a") == 0:
        print(-1)
    else:
        print(S.rfind("a")+1)

=======
Suggestion 6

def main():
    s = input()
    print(s.rfind('a'))

=======
Suggestion 7

def main():
    S = input()
    if S.rfind('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 8

def main():
    S = input()
    if S.find('a') != -1:
        print(S.rfind('a')+1)
    else:
        print(-1)

=======
Suggestion 9

def main():
    S = input()
    if "a" in S:
        print(S.rfind("a")+1)
    else:
        print(-1)

=======
Suggestion 10

def main():
    s = input()
    print(s.rfind('a')+1)
