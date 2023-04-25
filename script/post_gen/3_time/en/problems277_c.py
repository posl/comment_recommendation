Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    ans = 1
    for i in range(N-1, -1, -1):
        if ans % A[i] == 0:
            ans += B[i] - A[i]
        else:
            ans += B[i] - (ans % A[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))
    ladders.sort(key=lambda x: x[1])
    current_floor = 1
    for i in range(N):
        if ladders[i][0] >= current_floor:
            current_floor = ladders[i][1]
    print(current_floor)

=======
Suggestion 3

def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a, b = map(int, input().split())
        ladders.append([a, b])
    ladders.sort()
    #print(ladders)
    a = ladders[0][0]
    b = ladders[0][1]
    for i in range(1, n):
        if ladders[i][0] <= a and a <= ladders[i][1]:
            a = ladders[i][0]
            b = ladders[i][1]
        elif ladders[i][0] <= b and b <= ladders[i][1]:
            a = ladders[i][0]
            b = ladders[i][1]
        else:
            a = ladders[i][0]
            b = ladders[i][1]
    print(b)

=======
Suggestion 4

def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    print(ladders[-1][1])

=======
Suggestion 5

def main():
    n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    ladders.sort(key=lambda x: x[1])
    ans = 1
    for ladder in ladders:
        if ans < ladder[0]:
            ans = ladder[1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    max_floor = 0
    for i in range(N):
        if max_floor < ladders[i][1]:
            max_floor = ladders[i][1]
        else:
            max_floor = ladders[i][0]
    print(max_floor)

=======
Suggestion 7

def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[1])
    now = 0
    for i in range(N):
        if ladders[i][0] > now:
            now = ladders[i][0]
        else:
            now = ladders[i][1]
    print(now)

=======
Suggestion 8

def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 1
    for i in range(N):
        if ans < AB[i][0]:
            break
        ans = AB[i][1]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(N)]
    ladders.sort(key=lambda x: x[0])
    last_floor = ladders[0][0]
    for ladder in ladders:
        if ladder[0] != last_floor:
            print(last_floor)
            exit()
        last_floor = ladder[1]
    print(last_floor)

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # 1. Find the ladders that connect the highest floor (10**9)
    # 2. Find the ladders that connect the highest floor (10**9) from those ladders
    # 3. Repeat step 2 until there is no ladder that connects the highest floor (10**9)
    # 4. The highest floor that Takahashi can reach is the highest floor of the ladders that connect the highest floor (10**9)
    ladders = set(range(N))
    while True:
        next_ladders = set()
        for i in ladders:
            a, b = AB[i]
            if a == 10**9 or b == 10**9:
                next_ladders.add(i)
        if len(next_ladders) == 0:
            break
        ladders = next_ladders
    ans = 10**9
    for i in ladders:
        a, b = AB[i]
        ans = min(ans, a, b)
    print(ans)
