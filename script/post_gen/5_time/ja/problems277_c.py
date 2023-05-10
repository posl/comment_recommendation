Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    #print(AB)
    ans = 0
    for ab in AB:
        if ab[0] >= ans:
            ans = ab[1]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for i in range(N):
        if ans < AB[i][0]:
            ans = AB[i][1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        if ans < a:
            ans = b
    print(ans)
    return

=======
Suggestion 4

def solve():
    N = int(input())
    AB = [ tuple(map(int, input().split())) for _ in range(N) ]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for a, b in AB:
        if a > ans:
            ans = b
    print(ans)

solve()

=======
Suggestion 5

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 0
    for i in range(n):
        if ab[i][0] < ans:
            continue
        else:
            ans = ab[i][1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(N):
        if AB[i][0] < ans:
            continue
        ans = AB[i][1] - 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(min(a) + min(b))

=======
Suggestion 8

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
    if N % 2 == 1:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print((B[N // 2 - 1] + B[N // 2]) - (A[N // 2 - 1] + A[N // 2]) + 1)

=======
Suggestion 9

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for i in range(N):
        if ans < AB[i][0]:
            ans = AB[i][0]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append([A, B])
    ladders.sort(key=lambda x:x[1])
    current = -1
    count = 0
    for ladder in ladders:
        if current < ladder[0]:
            current = ladder[1]
            count += 1
    print(count)
