Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n-1,-1,-1):
        print(s[i])

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(n):
        print(input())

=======
Suggestion 8

def solve():
    n = int(input())
    for i in range(n):
        print(input())
