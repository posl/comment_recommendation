Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        s = s[0:k] + "..."
    print(s)

=======
Suggestion 2

def main():
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)

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
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')

=======
Suggestion 5

def main():
    k = int(input())
    s = input()
    if len(s)>k:
        print(s[:k]+"...")
    else:
        print(s)
main()

=======
Suggestion 6

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + "...")

=======
Suggestion 7

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + '...')

=======
Suggestion 8

def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[0:k] + "...")
    else:
        print(s)
