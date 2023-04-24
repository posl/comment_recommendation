Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if 'a' in S:
        print(len(S) - S[::-1].index('a'))
    else:
        print(-1)

=======
Suggestion 2

def main():
    S = input()
    if 'a' in S:
        print(S.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 3

def main():
    S = input()
    if S.find("a") == -1:
        print(-1)
    else:
        print(S.rfind("a")+1)

=======
Suggestion 4

def main():
    s = input()
    print(s.rfind('a')+1 if 'a' in s else -1)

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a') + 1 if s.find('a') != -1 else -1)

=======
Suggestion 6

def main():
    s = input()
    s = s[::-1]
    for i, c in enumerate(s):
        if c == 'a':
            print(len(s) - i)
            return
    print('-1')

=======
Suggestion 7

def main():
    S = input()
    print(S.rfind('a'))
