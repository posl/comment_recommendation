Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + "...")

=======
Suggestion 2

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + "...")

=======
Suggestion 3

def main():
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[0:K] + '...')

main()

=======
Suggestion 4

def main():
    k = int(input())
    s = input()
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + "...")

=======
Suggestion 5

def main():
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[:K] + '...')
    else:
        print(S)

=======
Suggestion 6

def main():
    # input
    K = int(input())
    S = input()

    # compute

    # output
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')

=======
Suggestion 7

def main():
    k = int(input())
    s = input()

    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

=======
Suggestion 8

def main():
    # Write your code here
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')
main()
