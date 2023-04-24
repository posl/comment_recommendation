Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if 'a' in s:
        print(len(s) - s[::-1].index('a'))
    else:
        print(-1)

=======
Suggestion 2

def main():
    S = input()
    if 'a' in S:
        print(len(S) - S[::-1].index('a'))
    else:
        print(-1)

=======
Suggestion 3

def main():
    S = input()
    if "a" in S:
        print(len(S) - S[::-1].index("a"))
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'a':
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    S = input()
    if 'a' in S:
        print(S.rindex('a') + 1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    s = input()
    if 'a' not in s:
        print(-1)
    else:
        print(len(s) - s[::-1].index('a'))

=======
Suggestion 7

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a') + 1)

=======
Suggestion 8

def main():
    s = input()
    if s.find('a') == -1:
        print(-1)
    else:
        print(s.rfind('a')+1)

=======
Suggestion 9

def main():
    S = input()
    if S.count("a") == 0:
        print(-1)
    else:
        print(S[::-1].index("a") + 1)

=======
Suggestion 10

def main():
    S = input()
    print(S.rfind('a') + 1)
