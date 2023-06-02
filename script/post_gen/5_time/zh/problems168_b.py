Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + "...")

=======
Suggestion 2

def printString(S,K):
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K]+'...')

=======
Suggestion 3

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[0:k] + "...")
    else:
        print(s)

=======
Suggestion 4

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

=======
Suggestion 5

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + '...')

=======
Suggestion 6

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + "...")

=======
Suggestion 7

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + "...")
