Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
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

    for i in range(n-1, -1, -1):
        print(s[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a.reverse()
    for i in range(n):
        print(a[i])

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 6

def main():
    N = int(input())
    strings = []
    for i in range(N):
        strings.append(input())
    strings.reverse()
    for string in strings:
        print(string)

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.reverse()
    print("\n".join(s))

=======
Suggestion 8

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.reverse()
    print(*s, sep='\n')

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(n):
        print(input())

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(n):
        print(input())
    return
