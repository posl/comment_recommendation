Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[1])
    current = 1
    for a, b in ladders:
        if a <= current <= b:
            current = b
    print(current)

solve()

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(max(A)+min(B))

=======
Suggestion 3

def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x:x[0])
    max_floor = 0
    for a, b in ladders:
        if max_floor < a:
            max_floor = b
    print(max_floor)

=======
Suggestion 4

def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a,b = map(int, input().split())
        ladders.append((min(a,b), max(a,b)))
    ladders.sort(key=lambda x: x[0])
    highest = 0
    for ladder in ladders:
        if ladder[0] > highest:
            break
        else:
            highest = max(highest, ladder[1])
    print(highest)

=======
Suggestion 5

def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[1])
    current = 1
    for ladder in ladders:
        if current < ladder[0]:
            current = ladder[0]
        current = ladder[1]
    print(current)

=======
Suggestion 6

def problem277_c():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))

    ladders = sorted(ladders, key=lambda x: x[1])
    print(ladders)
    print(ladders[0][1])

    for i in range(1, N):
        if ladders[i][0] > ladders[i-1][1]:
            print(ladders[i-1][1])
            return
    print(ladders[N-1][1])

=======
Suggestion 7

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1])
    print(AB[-1][1])

=======
Suggestion 8

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1], reverse=True)

    floor = ab[0][1]
    for i in range(1, n):
        if floor <= ab[i][0]:
            floor = ab[i][0] - 1
        else:
            floor = ab[i][1]
    print(floor)

=======
Suggestion 9

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(tuple(map(int, input().split())))

    A = sorted(ladders, key=lambda x: x[0])
    B = sorted(ladders, key=lambda x: x[1])

    print(max(A[-1][0], B[-1][1]))

=======
Suggestion 10

def solve(n, ladders):
    #print(n, ladders)
    ladders.sort(key=lambda x:x[0])
    #print(ladders)
    min_floor = 1
    max_floor = 10**9
    for ladder in ladders:
        a = ladder[0]
        b = ladder[1]
        if a > min_floor:
            min_floor = a
        if b < max_floor:
            max_floor = b
        if min_floor > max_floor:
            return 0
    return max_floor - min_floor + 1
