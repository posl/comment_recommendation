Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break

=======
Suggestion 2

def solve():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('Aoki')
    else:
        print('Takahashi')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if (i+1) % 2 == 0:
                print("Aoki")
            else:
                print("Takahashi")
            return

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S[0] == '0':
        print('Takahashi')
    else:
        if S.count('0') == 0:
            print('Aoki')
        else:
            print('Takahashi')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if "0" in S:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    print("Takahashi" if s.find("1") % 2 == 0 else "Aoki")

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[0] == "1":
        print("Aoki")
    else:
        print("Takahashi")

=======
Suggestion 9

def main():

    N = int(input())
    S = input()

    for i in range(N):
        if S[i] == "1":
            print("Aoki" if i % 2 == 0 else "Takahashi")
            break

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    print('Aoki' if S.find('1') % 2 == 0 else 'Takahashi')
