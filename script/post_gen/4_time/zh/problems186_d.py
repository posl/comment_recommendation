Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += (a[i] * (2 * i - n + 1))
    return ans

=======
Suggestion 2

def solve(n, a):
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i * 2 - n + 1)
    return ans

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] - A[i-1]
    print(ans*2)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += (A[i]*(2*i-N+1))
    print(sum)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    ans = 0
    for i in range(n):
        ans += a[i] * i - sum(a[:i])
        ans -= a[i] * (n - i - 1) - sum(a[i + 1:])
    print(ans)

=======
Suggestion 6

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += abs(a[i] - a[j])

    # 打印答案
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        sum += A[i] * i - A[i] * (N - i - 1)
    print(sum)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i - (n - 1 - i))
    print(ans * 2)

=======
Suggestion 10

def main():
    #N = 3
    #A = [5,1,2]
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - sum(A[:i])
        ans -= A[i] * (N - i - 1) - sum(A[i + 1:])
    print(ans)
