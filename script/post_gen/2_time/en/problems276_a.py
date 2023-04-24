Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 2

def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a') + 1)
    else:
        print('-1')

=======
Suggestion 3

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(len(S) - S[::-1].index('a') - 1)

=======
Suggestion 4

def main():
    S = input()
    print(S.rfind('a') + 1)

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a')+1)

=======
Suggestion 6

def main():
    s = input()
    print(s.rfind("a") + 1)

=======
Suggestion 7

def find_last(string, char):
    return string.rfind(char)
