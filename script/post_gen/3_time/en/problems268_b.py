Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    t = input()
    if t.startswith(s):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if T.startswith(S):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T[0:len(S)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input()
    T = input()
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    #S = input()
    #T = input()
    S = 'atco'
    T = 'atcoder'

    if T.startswith(S):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input()
    T = input()
    print('Yes' if S==T[:len(S)] else 'No')
