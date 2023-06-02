Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    work = []
    for i in range(N):
        a, b = map(int, input().split())
        work.append((a, b))
    work.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    #N = int(input())
    #AB = []
    #for i in range(N):
    #    AB.append(list(map(int, input().split())))
    N = 30
    AB = [[384, 8895], [1725, 9791], [170, 1024], [4, 11105], [2, 6], [578, 1815], [702, 3352], [143, 5141], [1420, 6980], [24, 1602], [849, 999], [76, 7586], [85, 5570], [444, 4991], [719, 11090], [470, 10708], [1137, 4547], [455, 9003], [110, 9901], [15, 8578], [368, 3692], [104, 1286], [3, 4], [366, 12143], [7, 6649], [610, 2374], [152, 7324], [4, 7042], [292, 11386], [334, 5720]]
    AB.sort(key=lambda x:x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print("No")
            exit()
    print("Yes")
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += ab[i][0]
        if time > ab[i][1]:
            print("No")
            break
    else:
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
    C = sorted(zip(A, B), key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += C[i][0]
        if t > C[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    #读取输入
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))

    #按照最后期限排序
    a_b.sort(key=lambda x:x[1])

    #计算完成时间
    time = 0
    for i in range(n):
        time += a_b[i][0]
        if time > a_b[i][1]:
            print("No")
            return

    print("Yes")

=======
Suggestion 6

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            return False
    return True

print('Yes' if solve() else 'No')

=======
Suggestion 7

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))

    AB.sort(key=lambda x:x[1])

    for i in range(N):
        if sum(map(lambda x:x[0], AB[:i+1])) > AB[i][1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def solve():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append([int(i) for i in input().split()])
    AB.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    N = int(input())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))

    work.sort(key=lambda x: x[1])

    time = 0
    for i in range(N):
        time += work[i][0]
        if time > work[i][1]:
            print("No")
            return
    print("Yes")
