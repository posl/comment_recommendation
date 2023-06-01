Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    jobs = []
    for i in range(N):
        a,b = map(int,input().split())
        jobs.append([a,b])
    jobs = sorted(jobs,key=lambda x:x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[1])

    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    time = 0
    for a, b in AB:
        time += a
        if time > b:
            print('No')
            return
    print('Yes')

=======
Suggestion 4

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    N = int(input())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for ab in AB:
        t += ab[0]
        if t > ab[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))

    AB.sort(key=lambda x: x[1])

    time = 0
    for ab in AB:
        time += ab[0]
        if time > ab[1]:
            print('No')
            return

    print('Yes')
    return

=======
Suggestion 7

def main():
    N = int(input())
    work = []
    for i in range(N):
        a, b = map(int, input().split())
        work.append((a, b))
    work = sorted(work, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 8

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x:x[1])
    current_time = 0
    for a, b in jobs:
        current_time += a
        if current_time > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print('No')
            return
    print('Yes')
