Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 2

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 3

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for j in jobs:
        time += j[1]
        if time > j[0]:
            print('No')
            return
    print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += ab[i][0]
        if t > ab[i][1]:
            print('No')
            exit()
    print('Yes')

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
    a.sort()
    b.sort()
    #print(a)
    #print(b)
    ans = 0
    for i in range(n):
        ans += a[i]
        if ans > b[i]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def solve():
    N = int(input())
    task = []
    for _ in range(N):
        a, b = map(int, input().split())
        task.append((a, b))
    task.sort(key=lambda x: x[1])
    time = 0
    for a, b in task:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")
solve()

=======
Suggestion 9

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    now = 0
    for i in range(N):
        now += AB[i][0]
        if now > AB[i][1]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 10

def main():
    #n = int(input())
    #a = list(map(int, input().split()))
    #a = [list(map(int, input().split())) for _ in range(n)]
    #s = input()
    #s = [input() for _ in range(n)]
    #n, m = map(int, input().split())
    #a = [list(map(int, input().split())) for _ in range(m)]
    #a = [int(input()) for _ in range(n)]
    #a = [list(map(int, input().split())) for _ in range(n)]
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x:x[1])
    t = 0
    for i in range(n):
        t += a[i][0]
        if t > a[i][1]:
            print('No')
            exit()
    print('Yes')
    #print(t)
    #print(a)
    #print('Yes')
    #print('No')
