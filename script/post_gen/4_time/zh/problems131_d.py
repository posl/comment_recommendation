Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += ab[i][0]
        if time > ab[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    job = [list(map(int, input().split())) for _ in range(N)]
    job.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += job[i][0]
        if time > job[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A, B))
    C.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += C[i][0]
        if t > C[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        C.append([B[i], A[i]])
    C.sort()
    t = 0
    for i in range(N):
        t += C[i][1]
        if t > C[i][0]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N = int(input())
    works = []
    for _ in range(N):
        A, B = map(int, input().split())
        works.append((A, B))
    works.sort(key=lambda x: x[1])

    time = 0
    for A, B in works:
        if time + A > B:
            print('No')
            break
        time += A
    else:
        print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    works = [list(map(int, input().split())) for i in range(n)]
    works.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += works[i][0]
        if time > works[i][1]:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print(len(A))
    #print(len(B))
    #print(max(B))
    #print(max(A))
    #print(sum(A))
    if max(B) < sum(A):
        print('No')
    else:
        print('Yes')

=======
Suggestion 8

def main():
    n = int(input())
    tasks = []
    for i in range(n):
        a, b = map(int, input().split())
        tasks.append((a, b))

    tasks.sort(key=lambda x: x[1])

    time = 0
    for task in tasks:
        time += task[0]
        if time > task[1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 9

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

solve()

=======
Suggestion 10

def my_sort(x):
    return x[1]

n = int(input())
list = []
for i in range(n):
    a, b = map(int, input().split())
    list.append([a, b])
list.sort(key=my_sort)
time = 0
for i in range(n):
    time += list[i][0]
    if time > list[i][1]:
        print("No")
        exit()
print("Yes")
