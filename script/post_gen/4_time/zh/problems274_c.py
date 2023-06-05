Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1

    #print(B)
    for i in range(1, 2*N+1):
        if i == 1:
            print(0)
        else:
            j = i
            count = 0
            while j != 1:
                j = B[j]
                count += 1
            print(count)

main()

=======
Suggestion 2

def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    # 生成结果
    ans = []
    for i in range(2 ** N):
        ans.append(0)
    for i in range(N):
        ans[2 * i] = 1
    for i in range(N):
        ans[A[i] - 1] = ans[i] + 1
    # 输出结果
    for i in range(2 ** N):
        print(ans[i])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    ans = [0]*(2*n+1)
    for i in range(1,2*n+1):
        j = i
        cnt = 0
        while j > 0:
            cnt += 1
            j //= 2
        ans[i] = cnt-1
    for i in range(1,2*n+1):
        j = i
        cnt = 0
        while j > 0:
            cnt += 1
            j //= 2
        ans[i] = cnt-1
    for i in range(2,2*n+1):
        if ans[i] == 1:
            ans[i] = ans[b[i]]+1
    for i in range(1,2*n+1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    from collections import deque
    Q = deque()
    Q.append((1, 0))
    while Q:
        i, d = Q.popleft()
        print(d)
        if 2 * i <= 2 * N and B[2 * i] != 0:
            Q.append((2 * i, d + 1))
        if 2 * i + 1 <= 2 * N and B[2 * i + 1] != 0:
            Q.append((2 * i + 1, d + 1))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = i
        while j > 1:
            j = j // 2
            B[i] += 1
    for i in range(1, 2*N+1):
        print(B[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        j = i
        cnt = 0
        while j > 0:
            j //= 2
            cnt += 1
        print(cnt - 1 + b[i])

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        j = i
        while j > 0:
            print(i-j)
            j = B[j]//2

=======
Suggestion 8

def solve(n, A):
    n = 2*n + 1
    B = [0]*n
    B[0] = 0
    for i in range(n-1):
        B[i+1] = B[(i+1)//2] + 1
    ans = []
    for i in range(n):
        ans.append(B[A[i]])
    return ans

n = int(input())
A = list(map(int, input().split()))
ans = solve(n, A)
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2*n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2*n + 1):
        j = i
        while j > 0 and b[j] < b[(j + 1) // 2]:
            b[j], b[(j + 1) // 2] = b[(j + 1) // 2], b[j]
            j = (j + 1) // 2
    for i in range(1, 2*n + 1):
        j = i
        ans = 0
        while j > 1:
            j //= 2
            ans += 1
        print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(2 * n - 1, 0, -1):
        ans[i // 2] = min(ans[i // 2], ans[i] + 1)
    for i in range(1, 2 * n + 1):
        print(ans[i])
