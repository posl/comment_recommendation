Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s.rfind("a") == -1:
        print(-1)
    else:
        print(s.rfind("a")+1)

=======
Suggestion 2

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a') + 1)

=======
Suggestion 3

def main():
    s = input()
    if s.count("a") == 0:
        print(-1)
    else:
        print(s.rfind("a")+1)

=======
Suggestion 4

def main():
    s = input()
    if "a" not in s:
        print(-1)
    else:
        print(s.rfind("a")+1)

=======
Suggestion 5

def solve():
    s = input()
    if 'a' in s:
        print(s.rindex('a') + 1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    s = input()
    try:
        print(s.rindex('a') + 1)
    except ValueError:
        print(-1)

=======
Suggestion 7

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 8

def main():
    s = input()
    print(s.rfind("a"))

=======
Suggestion 9

def solve():
    S = input()
    print(S.rfind('a'))
