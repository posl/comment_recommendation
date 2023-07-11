Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

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
    a = []
    for i in range(n):
        a.append(input())
    print(len(list(set(a))))

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(0,N):
        S.append(input(

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print(len(set(S)))

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    print(len(set(S)))

=======
Suggestion 8

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)
