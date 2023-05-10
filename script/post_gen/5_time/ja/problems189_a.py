Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    c1, c2, c3 = input().strip()
    if c1 == c2 and c1 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    c1,c2,c3 = input().rstrip().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def solve():
    # coding: utf-8
    # Your code here!
    #文字列の入力
    s = input()
    #出力
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 4

def main():
    C = input()
    if C[0] == C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def main():
    C = input()
    if C[0] == C[1] and C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    C_1, C_2, C_3 = input().split()
    if C_1 == C_2 and C_2 == C_3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 7

def main():
    c = input()
    if c[0] == c[1] and c[1] == c[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 8

def main():
    c1, c2, c3 = input()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 9

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 10

def main():
    # input
    C1, C2, C3 = input().split()

    # compute

    # output
    if C1 == C2 and C2 == C3:
        print("Won")
    else:
        print("Lost")
