Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([i for i in D if i <= X]))

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    print(len([i for i in d if i <= x]))

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)
main()

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])

    cnt = 0
    for d in D:
        if d <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    D = [0] * (N+1)
    for i in range(1, N+1):
        D[i] = D[i-1] + L[i-1]

    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
    print(count)

=======
Suggestion 7

def problems130_b():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(1, n + 1):
        d.append(d[i - 1] + l[i - 1])
    print(sum([1 for i in d if i <= x]))

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = 0
    for i in range(N):
        D += L[i]
        if D > X:
            print(i+1)
            exit()
    print(N+1)

=======
Suggestion 9

def problems130_b():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(len(l)):
        d += l[i]
        if d <= x:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    L = map(int, input().split())
    D = [0]
    for i in L:
        D.append(D[-1] + i)
    print(sum([1 for i in D if i <= X]))
