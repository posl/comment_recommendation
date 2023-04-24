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
            break
    else:
        print('No')

=======
Suggestion 3

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 4

def main():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

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
Suggestion 6

def solve():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

solve()

=======
Suggestion 7

def canDoDamage(N, S, D, spells):
    for spell in spells:
        if spell[0] < S or spell[1] > D:
            return "Yes"
    return "No"
