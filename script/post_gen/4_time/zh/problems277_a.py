Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input().split()[0])
    p = list(map(int, input().split()))
    x = int(input().split()[1])
    print(p.index(x)+1)

=======
Suggestion 2

def main():
    n,x=map(int,input().split())
    p=list(map(int,input().split()))
    for i in range(n):
        if p[i]==x:
            print(i+1)

=======
Suggestion 3

def findit(n,x,p):
    for i in range(n):
        if p[i] == x:
            return i+1

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 5

def get_input():
    n, x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    return n, x, p

=======
Suggestion 6

def find_x(p, x):
    for i in range(len(p)):
        if p[i] == x:
            return i + 1

=======
Suggestion 7

def main():
    line = input().split()
    N = int(line[0])
    X = int(line[1])
    P = input().split()
    for i in range(N):
        P[i] = int(P[i])
    for i in range(N):
        if P[i] == X:
            print(i+1)
            break

=======
Suggestion 8

def find_x(n,x,p):
    for i in range(n):
        if p[i]==x:
            return i+1

n,x=map(int,input().split())
p=list(map(int,input().split()))
print(find_x(n,x,p))

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == x:
            print(i + 1)
            break
