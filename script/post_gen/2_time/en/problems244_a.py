Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    print(S[-1])

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    print(s[-1])

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    print(S[N-1])

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    if n >= 1 and n <= 1000 and len(s) == n:
        print(s[-1])
    else:
        print('Invalid Input')

=======
Suggestion 5

def main():
    # read input
    N = int(input())
    S = input()

    # output
    print(S[N-1])

=======
Suggestion 6

def last_char(s):
    return s[-1]
