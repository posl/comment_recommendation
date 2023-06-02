Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    num = input().split()
    num = [int(i) for i in num]
    n = num[0]
    x = num[1]
    p = input().split()
    p = [int(i) for i in p]
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break

=======
Suggestion 2

def solve():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x)+1)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i+1)
            break
    return 0

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i + 1)
            break

=======
Suggestion 5

def main():
    n, x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    for i in range(n):
        if p[i] == x:
            print i + 1
            break

=======
Suggestion 6

def main():
    n,x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x)+1)

=======
Suggestion 7

def find_x(x, p):
    for i in range(len(p)):
        if p[i] == x:
            return i + 1

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    P = list(map(int,input().split()))
    print(P.index(X)+1)

=======
Suggestion 9

def main():
    line = input()
    n, x = line.split()
    n = int(n)
    x = int(x)
    p = input()
    p = p.split()
    for i in range(len(p)):
        p[i] = int(p[i])
    for j in range(len(p)):
        if p[j] == x:
            print(j+1)
            break
