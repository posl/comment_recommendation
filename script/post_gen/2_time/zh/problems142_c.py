Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join([str(x) for x in b]))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append((i+1, A[i]))
    B.sort(key=lambda x:x[1])
    for i in range(N):
        print(B[i][0], end=" ")
    print()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(" ".join(map(str, b)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join(map(str,b)))

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(' '.join(map(str, b)))

=======
Suggestion 7

def main():
    #读取数据
    n = int(input())
    a = list(map(int, input().split()))
    #创建一个数组，用于记录学生的学号
    ans = [0]*n
    #遍历a数组，将a[i]放到ans[a[i]-1]的位置
    for i in range(n):
        ans[a[i]-1] = i+1
    #输出结果
    print(' '.join(map(str, ans)))

=======
Suggestion 8

def solve(n, a):
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(n):
        ans[a[i]-1] = i+1
    return ans

n = int(input())
a = list(map(int, input().split()))
ans = solve(n, a)
print(*ans)

=======
Suggestion 9

def solve(n, a):
    b = [None] * n
    for i in range(n):
        b[a[i]-1] = i+1
    return b
