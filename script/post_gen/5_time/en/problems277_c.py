Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        print(B[int(N/2)] + B[int(N/2) - 1] - A[int(N/2)] - A[int(N/2) - 1] + 1)
    else:
        print(B[int(N/2)] - A[int(N/2)] + 1)

=======
Suggestion 2

def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[1])
    max_floor = ladders[0][1]
    for ladder in ladders[1:]:
        if ladder[0] < max_floor:
            max_floor = ladder[0]
    print(max_floor - 1)

=======
Suggestion 3

def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[0])
    print(ladders[-1][0] + ladders[-1][1])

=======
Suggestion 4

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    current_floor = 1
    for ladder in ladders:
        if ladder[0] > current_floor:
            current_floor = ladder[0]
        if ladder[1] >= current_floor:
            current_floor = ladder[1]
    print(current_floor)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N%2 == 0:
        print(B[N//2] + B[N//2-1] - A[N//2] - A[N//2-1] + 1)
    else:
        print(B[N//2] - A[N//2] + 1)

=======
Suggestion 6

def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders = sorted(ladders, key=lambda x: x[1])
    print(ladders[-1][1] - 1)

=======
Suggestion 7

def main():
    n = int(input())
    ladders = []
    for i in range(n):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    max_floor = ladders[0][0] + ladders[0][1] - 1
    for i in range(1, n):
        if ladders[i][0] >= max_floor:
            max_floor = ladders[i][0] + ladders[i][1] - 1
        elif ladders[i][1] >= max_floor:
            max_floor = ladders[i][1] + ladders[i][0] - 1
    print(max_floor)

=======
Suggestion 8

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))

    ladders.sort(key=lambda x: x[1])

    #print(ladders)

    current_floor = 1
    for ladder in ladders:
        if ladder[0] >= current_floor:
            current_floor = ladder[1]
        elif ladder[1] >= current_floor:
            current_floor = ladder[1]

    print(current_floor)

=======
Suggestion 9

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if ans < ab[i][1]:
            ans = ab[i][1]
    print(ans)

=======
Suggestion 10

def main():
    # input
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # compute
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if AB[i][0] < ans:
            continue
        else:
            ans = AB[i][1]

    # output
    print(ans)
