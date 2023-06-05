Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + "...")

=======
Suggestion 2

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + '...')

=======
Suggestion 3

def problem168_b():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

=======
Suggestion 4

def main():
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[0:K] + "...")
    else:
        print(S)

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
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + '...')
