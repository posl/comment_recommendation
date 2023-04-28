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
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(list(set(s))))

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(len(set(S)))

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))
