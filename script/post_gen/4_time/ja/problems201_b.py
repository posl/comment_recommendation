Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 2

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        s, t = input().split()
        t = int(t)
        mountains.append([s, t])
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 3

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append([S, T])

    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 4

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountain = input().split()
        mountains.append(mountain)
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 5

def main():
    n = int(input())
    mountains = [input().split() for _ in range(n)]
    mountains.sort(key=lambda x:int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    T2 = sorted(T, reverse=True)
    print(S[T.index(T2[1])])

main()

=======
Suggestion 7

def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(str, input().split())))
    m.sort(key=lambda x: int(x[1]), reverse=True)
    print(m[1][0])

=======
Suggestion 8

def main():
    N = int(input())
    mountain = []
    for _ in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: x[1], reverse=True)
    print(mountain[1][0])

=======
Suggestion 9

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s,t = input().split()
        t = int(t)
        d[t] = s

    t = sorted(d.keys(),reverse=True)
    print(d[t[1]])
