Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('高桥')
    else:
        print('青木')

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
    n = int(input())
    s = input()
    if s[0] == '0':
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    if s.count('1')%2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S[0] == '1' or N % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 1:
        print('高桥')
    else:
        print('青木')

=======
Suggestion 7

def main():
    # N = int(input())
    # S = input()
    N = 5
    S = '00101'
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print('高桥')
            else:
                print('青木')
            break

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    if S.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    if s[0] == "1":
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print("Takahashi")
    else:
        print("Aoki")
