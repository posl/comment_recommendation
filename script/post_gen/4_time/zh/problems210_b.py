Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    print("")

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('高桥')
    else:
        print('青木')

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    print("高桥" if S[0] == "0" else "青木")

=======
Suggestion 4

def solve():
    n = int(input())
    s = input()
    if s.count('1')%2 == 0:
        print('Takahashi')
    else:
        print('Aoki')
solve()

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    print('Takahashi' if S.find('1') % 2 == 0 else 'Aoki')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if S.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[0] == '0':
        print('Takahashi')
    elif s[0] == '1':
        print('Aoki')

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    if S.count("1") % 2 == 1:
        print("高桥")
    else:
        print("青木")

=======
Suggestion 10

def solve():

    N = int(input())
    S = input()
    if S.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')
