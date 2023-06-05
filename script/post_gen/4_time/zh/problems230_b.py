Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s.find('o') != -1 and s.find('x') != -1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s[0] == 'o' or s[1] == 'o' or s[2] == 'o':
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if 'o' in s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if s.count('o') == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    t = 'x'*100000
    print('Yes' if s in t else 'No')

=======
Suggestion 6

def solve(s):
    t = 'x' * 100000
    if s in t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    if s.find('o') != -1 and s.find('x') != -1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input()
    if s.find('o') >= 0 and s.find('x') >= 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s = input()
    if s.count('o') >= 1 and s.count('x') >= 1:
        print('Yes')
    else:
        print('No')
