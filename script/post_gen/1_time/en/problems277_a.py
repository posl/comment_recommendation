Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X) + 1)

main()

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    print(P.index(X) + 1)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if P[i] == X:
            print(i+1)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    p = list(map(int, input().split()))
    print(p.index(x) + 1)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N):
        if X == P[i]:
            print(i+1)
            break
