Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    print(s.replace('na', 'nya'))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    print(s.replace("na", "nya"))

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    print(S.replace("na", "nya"))

=======
Suggestion 5

def main():
    N = int(input())
    S = input()

    S = S.replace('na', 'nya')
    print(S)

=======
Suggestion 6

def problem():
    N = int(input())
    S = input()
    print(S.replace('na', 'nya'))

problem()

=======
Suggestion 7

def f(N,S):
    if N < 2:
        return S
    elif N == 2:
        if S == 'na':
            return 'nya'
        else:
            return S
    else:
        if S[0:2] == 'na':
            return 'nya' + f(N-2, S[2:])
        else:
            return S[0] + f(N-1, S[1:])
