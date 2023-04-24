Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ladders = []
    for _ in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[0], reverse=True)
    ans = 1
    for a, b in ladders:
        if a <= ans:
            ans = b
        elif b <= ans:
            ans = a
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort()
    print(ladders[-1][1])

=======
Suggestion 3

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ladders = [[] for _ in range(10**9+1)]
    for i in range(N):
        ladders[A[i]].append(B[i])
        ladders[B[i]].append(A[i])
    for i in range(1, 10**9+1):
        ladders[i].sort()
    q = deque()
    q.append(1)
    visited = [False]*(10**9+1)
    visited[1] = True
    while q:
        v = q.popleft()
        for w in ladders[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
    for i in range(10**9, 0, -1):
        if visited[i]:
            print(i)
            break

=======
Suggestion 4

def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders.sort(key=lambda x: x[1])
    ans = 1
    for a, b in ladders:
        if ans < a:
            ans = b
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    for i in range(N):
        if ladders[i][0] > ladders[i][1]:
            ladders[i][0], ladders[i][1] = ladders[i][1], ladders[i][0]

    floor = 1
    for i in range(N):
        if ladders[i][0] <= floor <= ladders[i][1]:
            floor = ladders[i][1]
    print(floor)

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for a, b in AB:
        if a <= ans:
            ans = b
        else:
            ans = a
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ladders = [tuple(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[0])
    pos = 1
    for a, b in ladders:
        if a <= pos <= b:
            pos = b if a == pos else a
    print(pos)

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])

    current = 1
    for a, b in AB:
        if current < a:
            current = a
        elif current < b:
            current = b
        else:
            print(1)
            return

    print(current)

=======
Suggestion 9

def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]

    # Sort the ladders by the second element (the higher floor)
    ladders.sort(key=lambda x: x[1])

    # The highest floor that Takahashi can reach
    highest_floor = 1

    # For each ladder
    for i in range(n):
        # If the ladder's lower floor is higher than the current highest floor
        if ladders[i][0] > highest_floor:
            # Then he can't reach the higher floor using the ladder
            continue
        # Otherwise, update the highest floor
        highest_floor = ladders[i][1]

    # Print the highest floor that Takahashi can reach
    print(highest_floor)

=======
Suggestion 10

def readInt():
    return int(input())
