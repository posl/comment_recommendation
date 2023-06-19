Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x*(r-l+1))
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        l = i
        r = i
        x = a[i]
        while l > 0 and a[l-1] >= x:
            l -= 1
        while r < n-1 and a[r+1] >= x:
            r += 1
        ans = max(ans, x*(r-l+1))
    print(ans)

=======
Suggestion 4

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))

    # 输出结果
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for l in range(N):
        x = A[l]
        for r in range(l, N):
            x = min(x, A[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    max = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(A[i],A[j]+1):
                sum = 0
                for l in range(i,j+1):
                    if A[l] >= k:
                        sum += k
                    else:
                        sum += A[l]
                if sum > max:
                    max = sum
    print(max)
