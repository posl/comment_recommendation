Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 4

def main():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 6

def main():
    #入力
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #処理
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    #入力
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #処理
    for i in range(N):
        if X[i] >= S and Y[i] > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def main():
    N, S, D = map(int, input().split())
    for n in range(N):
        X, Y = map(int, input().split())
        if X < S and D < Y:
            print('Yes')
            return
    print('No')

=======
Suggestion 9

def main():
    N, S, D = map(int, input().split())
    for _ in range(N):
        if S < int(input().split()[0]) and int(input().split()[1]) > D:
            print('Yes')
            return
    print('No')
