Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[1])
    print(ab[-1][1]-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    print(min(b)-max(a)+1 if min(b)-max(a)+1>0 else 0)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort(reverse=True)
    print(max(A[0], B[0]))

=======
Suggestion 4

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n % 2 == 1:
        ans = b[n // 2] - a[n // 2] + 1
    else:
        ans = (b[n // 2 - 1] + b[n // 2]) - (a[n // 2 - 1] + a[n // 2]) + 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    #A.sort()
    #B.sort()
    #print(A)
    #print(B)

    if N == 1:
        print(max(A[0], B[0]))
        return

    A.sort()
    B.sort()
    #print(A)
    #print(B)

    if N % 2 == 1:
        print(max(A[N//2], B[N//2]))
    else:
        print(max(A[N//2-1], B[N//2-1], A[N//2], B[N//2]))

=======
Suggestion 6

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n % 2 == 0:
        print(b[n//2-1] + b[n//2] - a[n//2-1] - a[n//2] + 1)
    else:
        print(b[n//2] - a[n//2] + 1)

=======
Suggestion 7

def solution():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    #print(ab)
    ans = 1
    for i in range(n):
        if ab[i][0] < ans <= ab[i][1]:
            ans = ab[i][1] + 1
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))

    # 从最高楼层开始，逐层向下检查
    # 当前楼层
    cur_floor = 10**9
    # 梯子编号
    cur_ladder = 0

    # 逐层向下检查
    while True:
        # 如果当前楼层是1层，则停止检查
        if cur_floor == 1:
            break

        # 逐个检查梯子
        for i in range(n):
            # 如果当前楼层在梯子的上端，则移动到下端
            if cur_floor == ab[i][1]:
                cur_floor = ab[i][0]
                cur_ladder = i + 1
                break
            # 如果当前楼层在梯子的下端，则移动到上端
            elif cur_floor == ab[i][0]:
                cur_floor = ab[i][1]
                cur_ladder = i + 1
                break

    # 输出结果
    print(cur_ladder)

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
    A.sort()
    B.sort()
    if N % 2 == 0:
        ans = B[N // 2 - 1] + B[N // 2] - A[N // 2 - 1] - A[N // 2] + 1
    else:
        ans = B[N // 2] - A[N // 2] + 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))

    ab = sorted(ab, key=lambda x: x[1])

    cur = 0
    for i in range(n):
        if cur < ab[i][0]:
            cur = ab[i][1]

    print(cur)
