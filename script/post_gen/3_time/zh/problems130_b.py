Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    input = raw_input()
    input = input.split()
    n = int(input[0])
    x = int(input[1])
    input = raw_input()
    input = input.split()
    l = map(int,input)
    return n,x,l

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    cnt = 0
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
    print(cnt+1)

=======
Suggestion 3

def main():
    line = input()
    line = line.split()
    N = int(line[0])
    X = int(line[1])
    line = input()
    line = line.split()
    L = [int(x) for x in line]
    D = [0]*(N+1)
    for i in range(1,N+1):
        D[i] = D[i-1]+L[i-1]
    D.append(D[N]+L[N-1])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)
    return 0

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = [int(x) for x in input().split()]
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([x for x in D if x <= X]))

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(0,n):
        d.append(d[i]+l[i])
    for i in range(0,n+1):
        if d[i] > x:
            print(i)
            return
    print(n+1)

=======
Suggestion 6

def bounce(N, X, L):
    D = 0
    count = 0
    for i in range(N):
        D = D + L[i]
        if D <= X:
            count = count + 1
    return count + 1

=======
Suggestion 7

def problem130_b():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
    cnt = 0
    for i in range(N + 1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def input():
    n,x = map(int,raw_input().split())
    l = map(int,raw_input().split())
    return n,x,l

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += l[i]
        if sum > x:
            print(i+1)
            break
    else:
        print(n+1)

=======
Suggestion 10

def main():
    n,x = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]*(n+1)
    for i in range(1,n+1):
        D[i] = D[i-1] + L[i-1]
    for i in range(n+1):
        if D[i] > x:
            print(i)
            return
