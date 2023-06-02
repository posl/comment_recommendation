Synthesizing 9/10 solutions

=======
Suggestion 1

def problems142_c():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(" ".join([str(i) for i in b]))

=======
Suggestion 2

def get_order(n, a):
    order = []
    for i in range(n):
        order.append(a.index(i+1)+1)
    return order

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    print(*b)

=======
Suggestion 5

def solve():
    # 读入
    N = int(input())
    # A = [int(input()) for i in range(N)]
    A = list(map(int, input().split()))

    # 数组B，用于记录A中的数是否已经被遍历过
    B = [False] * N
    # 数组C，用于记录学生进入教室的顺序
    C = [0] * N
    # 遍历A中的每个数
    for i in range(N):
        # 如果A[i]没有被遍历过
        if not B[A[i]-1]:
            # 将A[i]加入数组C
            C[i] = A[i]
            # 将A[i]标记为已经被遍历过
            B[A[i]-1] = True
        else:
            # 如果A[i]已经被遍历过，那么就从前往后遍历数组B，找到第一个没有被遍历过的数，将它加入数组C
            for j in range(N):
                if not B[j]:
                    C[i] = j + 1
                    B[j] = True
                    break
    # 打印数组C
    print(' '.join(map(str, C)))

solve()

=======
Suggestion 6

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    return b

=======
Suggestion 7

def readinput():
    n = int(input())
    a = list(map(int,input().split()))
    return n,a

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.insert(a[i]-1, i+1)
    print(" ".join(map(str, b)))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(1,N+1):
        B.append((A[i-1],i))
    B.sort()
    for i in range(N):
        print(B[i][1],end=' ')
