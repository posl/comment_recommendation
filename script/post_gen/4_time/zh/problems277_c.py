Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    return n, a, b

=======
Suggestion 2

def solve():
    #读取输入
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int,input().split())
    #按照梯子的最高层排序
    AB = sorted(zip(A,B),key=lambda x:x[1])
    #print(AB)
    #开始遍历梯子
    now = 0
    for a,b in AB:
        if now < a:
            now = b
    print(now)

=======
Suggestion 3

def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    A.sort()
    B.sort()

    if N % 2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(B[N//2] + B[N//2 - 1] - A[N//2] - A[N//2 - 1] + 1)

=======
Suggestion 4

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    for i in range(n):
        if ans < ab[i][0]:
            ans = ab[i][0]
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split()
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    a.sort()
    b.sort()
    if n % 2 == 0:
        print(b[n // 2] - a[n // 2] + b[n // 2 - 1] - a[n // 2 - 1] + 1)
    else:
        print(b[n // 2] - a[n // 2] + 1)

=======
Suggestion 6

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))

    ab.sort(key=lambda x:x[1])

    ans = 1
    for i in range(n):
        if ab[i][0] < ans <= ab[i][1]:
            ans = ab[i][1] + 1

    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    ans = 1
    for a, b in ab:
        if ans < a:
            ans = b
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    #print(AB)
    ans = 0
    for i in range(N):
        if AB[i][0] <= ans and AB[i][1] > ans:
            ans = AB[i][1]
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    min = 1
    max = 10**9
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]

    if min > max:
        print(0)
    else:
        print(max - min + 1)

=======
Suggestion 10

def main():
    N = int(input())
    #A, B = [0 for i in range(N)], [0 for i in range(N)]
    #for i in range(N):
    #    A[i], B[i] = map(int, input().split())
    #A.sort()
    #B.sort()
    #print(A)
    #print(B)
    A, B = zip(*[tuple(map(int, input().split())) for i in range(N)])
    A = sorted(A)
    B = sorted(B)
    print(A)
    print(B)
    if N % 2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(B[N//2-1] + B[N//2] - A[N//2-1] - A[N//2] + 1)
