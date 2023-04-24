Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def main():
    S = input()
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    S = input()
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 4

def main():
    s = input()
    if (s[0] == s[1] and s[1] == s[2]) or (s[1] == s[2] and s[2] == s[3]):
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Bad")
    elif s[1] == s[2] == s[3]:
        print("Bad")
    elif s[0] == s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] == s[3]:
        print("Bad")
    elif s[0] == s[1] == s[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 6

def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[3]:
        print("Bad")
    elif S[0] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    # input
    S = input()

    # compute

    # output
    if S[0] == S[1] == S[2] or S[1] == S[2] == S[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 8

def main():
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[1] == S[2]:
        print("Bad")
    elif S[1] == S[2] and S[2] == S[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 9

def main():
    # input
    S = input()

    # compute

    # output
    if S[0] == S[1] == S[2] == S[3]:
        print('Bad')
    elif S[0] != S[1] != S[2] != S[3]:
        print('Good')
    else:
        print('Bad')

=======
Suggestion 10

def solve():
    # === 数値の入力 ===
    #n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    # === 行列の入力 ===
    #a = [list(map(int, input().split())) for _ in range(n)]
    S = input()
    if S[0] == S[1] == S[2] == S[3]:
        print('Bad')
    elif S[1] == S[2] == S[3]:
        print('Bad')
    elif S[0] == S[1] == S[2]:
        print('Bad')
    else:
        print('Good')
    return
