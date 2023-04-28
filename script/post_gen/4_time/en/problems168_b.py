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
        print(S[:K] + '...')

=======
Suggestion 4

def main():
    # input
    K = int(input())
    S = input()

    # compute
    if len(S) <= K:
        ans = S
    else:
        ans = S[:K] + '...'

    # output
    print(ans)

=======
Suggestion 5

def main():
    #input
    K = int(input())
    S = input()

    #output
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')

=======
Suggestion 6

def main():
    k = int(input())
    s = input()
    if k < len(s):
        print(s[:k] + "...")
    else:
        print(s)

=======
Suggestion 7

def main():
    # get input
    k = int(input())
    s = input()

    # check length of s
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + "...")
