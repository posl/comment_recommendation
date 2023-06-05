Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if a[i] >= max:
            count += 1
            max = a[i]
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    max_h = 0
    ans = 0
    for i in range(N):
        if max_h <= A[i]:
            ans += max_h - A[i]
            max_h = A[i]
        else:
            max_h = A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        A[i] -= i
    A.sort()
    if N % 2 == 1:
        b = A[N // 2]
    else:
        b = (A[N // 2] + A[N // 2 - 1]) // 2
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

=======
Suggestion 4

def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-1,-1,-1):
        if a[i]>ans:
            ans=a[i]
        else:
            if (ans-a[i])%2==1:
                ans=a[i]-1
    print(ans)
main()

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)

    # 从最后一个人开始，往前看，如果比前一个人高，那么就把前一个人的高度加1
    # 如果比前一个人矮，那么就把前一个人的高度减到和当前人一样高
    # 这样一直到第一个人，就是最小的总高度
    # 注意，如果前一个人比当前人高，那么前一个人的高度减到和当前人一样高，那么前面的人也可能会变矮，所以要一直往前看
    height = 0
    for i in range(N - 1, 0, -1):
        if A[i] > A[i - 1]:
            height += A[i] - A[i - 1]
        elif A[i] < A[i - 1]:
            A[i - 1] = A[i]

    print(height)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    maxA = max(A)
    #print(maxA)
    if maxA > N:
        print(0)
    else:
        print(maxA)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    B[0] = 0
    for i in range(1, N):
        if A[i - 1] < A[i]:
            B[i] = B[i - 1] + 1
        else:
            B[i] = 0
    #print(B)
    ans = 0
    for i in range(N):
        ans += B[i]
    print(ans)

=======
Suggestion 8

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    b=[0 for i in range(n)]
    b[0]=a[0]
    for i in range(1,n):
        if a[i]>b[i-1]:
            b[i]=a[i]
        else:
            b[i]=b[i-1]
    b.reverse()
    print(sum(b))
main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = a[0]
    for i in range(1, n):
        b[i] = max(b[i - 1], a[i])
    c = 0
    for i in range(n - 1, -1, -1):
        if b[i] > a[i]:
            c += b[i] - a[i]
        if b[i] <= a[i]:
            b[i] = a[i]
    print(c)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(0, a[i] - a[i-1])
    print(ans)
