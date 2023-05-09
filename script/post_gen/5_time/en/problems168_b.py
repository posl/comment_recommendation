Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + "...")

=======
Suggestion 2

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + '...')

=======
Suggestion 3

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + '...')

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
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[0:K] + "...")
    else:
        print(S)

=======
Suggestion 6

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K]+"...")

=======
Suggestion 7

def main():
    K = int(input())
    S = input()

    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)

=======
Suggestion 8

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        s = s[:k] + "..."
    print(s)
