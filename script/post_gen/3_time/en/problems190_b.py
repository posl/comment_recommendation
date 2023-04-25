Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 2

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            exit()
    print('No')
    return

main()

=======
Suggestion 4

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    N,S,D = map(int,input().split())
    for i in range(N):
        X,Y = map(int,input().split())
        if X<S and D<Y:
            print("Yes")
            return
    print("No")
