Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = input().split()
    S = ""
    for i in range(1, 27):
        S += chr(P.index(str(i)) + 97)
    print(S)

=======
Suggestion 2

def main():
    P = list(map(int, input().split()))
    print(''.join([chr(ord('a') + p - 1) for p in P]))

=======
Suggestion 3

def main():
    P = [int(i) for i in input().split()]
    S = [chr(i+96) for i in P]
    print(''.join(S))

=======
Suggestion 4

def main():
    P = list(map(int, input().split()))
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(P)):
        print(S[P[i]-1], end = "")
    print("")

=======
Suggestion 5

def main():
    P = input().split()
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(S[int(P[i])-1],end="")
    print()

=======
Suggestion 6

def main():
    p = input().split()
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        print(s[int(p[i])-1], end='')
    print()

=======
Suggestion 7

def main():
    P = input().split()
    P = [int(i) for i in P]
    P = [chr(i + 96) for i in P]
    print("".join(P))

=======
Suggestion 8

def main():
    P = input()
    P = P.split(' ')
    P = [int(i) for i in P]
    S = ''
    for i in range(26):
        S += chr(P.index(i+1)+97)
    print(S)

=======
Suggestion 9

def main():
    P = list(map(int, input().split()))
    #print(P)
    S = ""
    for i in range(26):
        S += chr(P[i] + 96)
    print(S)

=======
Suggestion 10

def main():
    P = map(int, raw_input().split())
    S = [chr(96 + p) for p in P]
    print ''.join(S)
