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
    for i in range(N):
        for j in range(N - 1 - i):
            if B[j] > B[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                B[j], B[j + 1] = B[j + 1], B[j]
    time = 0
    for i in range(N):
        time += A[i]
        if time > B[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append([A, B])
    jobs.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    work.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print('No')
            return
    print('Yes')

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
    AB = []
    for i in range(N):
        AB.append([A[i], B[i]])
    AB.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def main():
    N = int(input())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    work = sorted(work, key=lambda x: x[1])
    time = 0
    for a, b in work:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 仕事を終わらせるまでの時間の短い順に並べる
    # 仕事を終わらせるまでの時間が同じなら、仕事の〆切が早い順に並べる
    # 仕事を終わらせるまでの時間と仕事の〆切が同じなら、仕事の番号が小さい順に並べる
    # 仕事番号は 1 から N までの整数なので、仕事番号が小さい順に並べると、
    # 仕事番号が小さい順に仕事を終わらせることになる
    # 仕事番号が小さい順に仕事を終わらせると、
    # 仕事番号が小さい順に仕事を終わらせることになる
    # 仕事番号が小さい順に仕事を終わらせると、
    # 仕事番号が小さい順に仕事を終わらせることになる
    # 仕事番号が小さい順に仕事を終わらせると、
    # 仕事番号が小さい順に仕事を終わらせることになる
    # 仕事番号が小さい順に仕事を終わらせると、
    # 仕事番号が小さい順に仕事を終わらせることになる
    # 仕事番号が小さい順に仕事を終わらせると、
    #

=======
Suggestion 7

def main():
    N = int(input())
    work = []
    for i in range(N):
        A, B = map(int, input().split())
        work.append([B, A])
    work.sort()

    time = 0
    for i in range(N):
        time += work[i][1]
        if time > work[i][0]:
            print("No")
            return

    print("Yes")

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
    A = list(reversed(A))
    B = list(reversed(B))
    t = 0
    for i in range(N):
        if t <= B[i]:
            t = B[i]
        else:
            t -= t % A[i]
        if t > B[i]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]

    AB.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    task = sorted(task, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += task[i][0]
        if time > task[i][1]:
            print('No')
            return
    print('Yes')
