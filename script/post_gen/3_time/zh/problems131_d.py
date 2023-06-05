Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    jobs = [list(map(int, input().split())) for i in range(n)]
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 2

def main():
    # 读取输入
    n = int(input())
    ab_list = []
    for i in range(n):
        ab_list.append(list(map(int, input().split())))
    ab_list.sort(key=lambda x:x[1])

    # 计算
    time = 0
    for i in range(n):
        time += ab_list[i][0]
        if time > ab_list[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    jobs = []
    for i in range(n):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key = lambda x:x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    list = []
    for i in range(N):
        A, B = map(int, input().split())
        list.append([A, B])
    list.sort(key=lambda x: x[1])
    sum = 0
    for i in range(N):
        sum += list[i][0]
        if sum > list[i][1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 7

def solve():
    n = int(input())
    works = []
    for i in range(n):
        a,b = map(int,input().split())
        works.append((a,b))
    works.sort(key=lambda x:x[1])
    now = 0
    for i in range(n):
        if now + works[i][0] > works[i][1]:
            print("No")
            return
        else:
            now += works[i][0]
    print("Yes")
    return

=======
Suggestion 8

def main():
    n = int(input())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append([a, b])
    ab.sort(key=lambda x: x[1])
    cur = 0
    for i in range(n):
        cur += ab[i][0]
        if cur > ab[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 9

def solve():
    # 读入数据
    N = int(input())
    task = []
    for i in range(N):
        task.append(list(map(int, input().split())))

    # 按照最后期限排序
    task.sort(key=lambda x: x[1])

    # 从最后期限小的开始做
    t = 0
    for i in range(N):
        t += task[i][0]
        if t > task[i][1]:
            print("No")
            return
    print("Yes")

solve()

=======
Suggestion 10

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x:x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")
    return
