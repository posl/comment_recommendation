Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print('Takahashi' if s[0] == '1' else 'Aoki')

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('高桥')
    else:
        print('青木')

=======
Suggestion 5

def solve():
    n = int(input())
    s = input()
    if s[n-1] == '0':
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if S.find('1')%2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if '1' in S[::2]:
        print('高桥')
    else:
        print('青木')
