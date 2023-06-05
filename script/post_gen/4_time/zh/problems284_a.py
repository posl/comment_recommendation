Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n-1,-1,-1):
        print(s[i])

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        print(s[-i-1])

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(N):
        print(input())

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n-1,-1,-1):
        print(s[i])

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-1-i])

=======
Suggestion 7

def main():
    N = int(input())
    list = []
    for i in range(N):
        list.append(input())
    list.reverse()
    print('\n'.join(list))

=======
Suggestion 8

def main():
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])
