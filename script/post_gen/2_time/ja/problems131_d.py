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
    A, B = zip(*sorted(zip(A, B)))

    time = 0
    for i in range(N):
        time += A[i]
        if time > B[i]:
            print("No")
            return
    print("Yes")

main()

=======
Suggestion 2

def main():
    N = int(input())
    work = []
    for i in range(N):
        A, B = map(int, input().split())
        work.append([A, B])
    work = sorted(work, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 3

def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

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
Suggestion 5

def solve():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    job = []
    for i in range(n):
        a, b = map(int, input().split())
        job.append([b, a])
    job.sort()
    time = 0
    for i in range(n):
        time += job[i][1]
        if time > job[i][0]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 7

def main():
    N = int(input())
    work = []
    for i in range(N):
        a, b = map(int, input().split())
        work.append([a, b])
    work.sort(key=lambda x: x[1]) # B_iでソート
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]: # 〆切を過ぎたらNo
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1]) # 仕事の〆切でソート
    now = 0
    for a, b in AB:
        now += a
        if now > b:
            print('No')
            return
    print('Yes')

=======
Suggestion 9

def main():
    N = int(input())
    work = []
    for i in range(N):
        a,b = map(int, input().split())
        work.append((b,a))
    work.sort()
    time = 0
    for i in range(N):
        time += work[i][1]
        if time > work[i][0]:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #仕事の終了時間でソート
    AB.sort(key=lambda x: x[1])
    #print(AB)
    #仕事の終了時間が早い順に仕事を終わらせる
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print('No')
            return
    print('Yes')
    return
