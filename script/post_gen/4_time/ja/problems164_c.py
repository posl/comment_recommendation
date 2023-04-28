Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

=======
Suggestion 4

def main():
    # input
    N = int(input())
    Ss = [input() for _ in range(N)]

    # compute
    Ss = set(Ss)

    # output
    print(len(Ss))

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    print(len(s))

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(len(set(S)))

=======
Suggestion 7

def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())

    print(len(s))
