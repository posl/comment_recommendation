Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    jobs = []
    for _ in range(n):
        a, b = map(int, input().split())
        jobs.append((b, a))
    jobs.sort()
    time = 0
    for b, a in jobs:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    time = 0
    for a, b in AB:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    N = int(input())
    jobs = []
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for job in jobs:
        time += job[1]
        if time > job[0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for job in jobs:
        time += job[1]
        if time > job[0]:
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
        jobs.append([B, A])
    jobs.sort()
    time = 0
    for B, A in jobs:
        time += A
        if time > B:
            print("No")
            return
    print("Yes")
    return

main()

This is my first post on my blog. I am going to write about the problems that I have solved on AtCoder.

I am going to start with the problems from the ABC 131 contest. I have solved 5 problems from this contest. I will write about the problems that I have solved.

I have solved the C and D problems. The C problem was easy. The D problem was a bit difficult. I have solved this problem using the greedy algorithm. I did not know about the greedy algorithm before this contest. I have learnt about this algorithm from this problem. I have solved this problem in Python. I will post the code for this problem in my next post.

This is my first post on my blog. I am going to write about the problems that I have solved on AtCoder. I am going to start with the problems from the ABC 131 contest. I have solved 5 problems from this contest. I will write about the problems that I have solved. I have solved the C and D problems. The C problem was easy. The D problem was a bit difficult. I have solved this problem using the greedy algorithm. I did not know about the greedy algorithm before this contest. I have learnt about this algorithm from this problem. I have solved this problem in Python. I will post the code for this problem in my next post.

=======
Suggestion 6

def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((B, A))
    jobs.sort()
    time = 0
    for B, A in jobs:
        time += A
        if time > B:
            print("No")
            return
    print("Yes")

=======
Suggestion 8

def main():
    #input
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())

    #solve
    #sort by B
    sort = sorted(enumerate(B),key=lambda x:x[1])
    #print(sort)
    time = 0
    for i in range(N):
        time += A[sort[i][0]]
        if time > sort[i][1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    N = int(input())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int,input().split())))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]

    jobs.sort(key=lambda x: x[1])

    current_time = 0
    for a, b in jobs:
        current_time += a
        if current_time > b:
            print('No')
            return
    print('Yes')
