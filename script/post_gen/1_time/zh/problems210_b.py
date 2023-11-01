Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == '1':
            if i % 2 == 0:

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 6

def main():
    num = int(input())
    str = input()
    count = 0
    for i in range(0,num):
        if str[i] == '0':
            count

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if '1' in s[::2]:
        print('Takahashi')
    else:
        print('Aoki')
