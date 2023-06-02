Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 1:
        print('高桥')
    else:
        print('青木')

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('高桥')
    else:
        print('青木')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    if S.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 5

def problem210_b():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 0:
        print('高桥')
    else:
        print('青木')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 0:
        print('高桥')
    else:
        print('青木')
