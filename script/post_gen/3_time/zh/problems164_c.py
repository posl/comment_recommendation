Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))
solve()

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 5

def main():
    n = int(input())
    items = []
    for i in range(n):
        items.append(input())
    print(len(set(items)))

=======
Suggestion 6

def solve():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 7

def main():
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    print(len(s))

=======
Suggestion 8

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))
