Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 2

def main():
    c1, c2, c3 = input()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    c1, c2, c3 = input()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 4

def main():
    C = input()
    if C[0] == C[1] and C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def main():
    slot = input()
    if slot[0] == slot[1] == slot[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    # input
    S = input()

    # compute

    # output
    if S[0]==S[1]==S[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 7

def main():
    c1, c2, c3 = input()
    print('Won' if c1 == c2 == c3 else 'Lost')

=======
Suggestion 8

def main():
    #input
    C1, C2, C3 = map(str, input().split())

    #compute

    #output
    if C1==C2 and C2==C3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 9

def main():
    #input
    C1,C2,C3 = input()

    #output
    if C1==C2 and C2==C3:
        print('Won')
    else:
        print('Lost')
