Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(n - 2):
        d1, d2 = map(int, input().split())
        d3, d4 = map(int, input().split())
        d5, d6 = map(int, input().split())
        if d1 == d2 and d3 == d4 and d5 == d6:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return

    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and D[i + 2][0] == D[i + 2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 5

def main():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2):
        if d[i][0] == d[i][1] == d[i + 1][0] == d[i + 1][1] == d[i + 2][0] == d[i + 2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 7

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i] == D[i+1] == D[i+2]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    D = [input().split() for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n-2):
        if l[i][0] == l[i][1] == l[i+1][0] == l[i+1][1] == l[i+2][0] == l[i+2][1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    N = int(input())
    ans = "No"
    for i in range(N-2):
        D = [int(x) for x in input().split()]
        if D[0] == D[1]:
            D = [int(x) for x in input().split()]
            if D[0] == D[1]:
                D = [int(x) for x in input().split()]
                if D[0] == D[1]:
                    ans = "Yes"
                    break
    print(ans)
