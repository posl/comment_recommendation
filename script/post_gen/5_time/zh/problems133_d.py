Synthesizing 10/10 solutions

=======
Suggestion 1

def problem133_d():
    pass

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    result = []
    for i in range(N):
        if i%2 == 0:
            result.append(sum(A[0:N:2]))
        else:
            result.append(sum(A[1:N:2]))
    print(' '.join(map(str,result)))

=======
Suggestion 3

def solve(n, a):
    s = sum(a)
    ans = []
    for i in range(n):
        ans.append(2*a[i] - s)
    return ans

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    for i in range(1, N):
        B[i] = A[i - 1] * 2 - B[i - 1]
    print(B[0], end='')
    for i in range(1, N):
        print(' ', B[i], end='')
    print()

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(N):
        if i % 2 == 0:
            B[0] += A[i]
        else:
            B[0] -= A[i]
    B[0] //= 2
    for i in range(1, N):
        B[i] = A[i - 1] - B[i - 1]
    for i in range(N):
        if i == N - 1:
            print(B[i])
        else:
            print(B[i], end=' ')

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == 0:
            print(A[i] - A[N-1], end=" ")
        else:
            print(A[i] - A[i-1], end=" ")

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] - sum(ans) // 2
    print(*ans)

=======
Suggestion 8

def solve(n, a):
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    # 4. 打印结果
    # 1. 计算所有山地的雨水量
    # 2. 计算所有水坝的雨水量
    # 3. 计算所有山地的雨水量
    #

=======
Suggestion 9

def compute_rainfall(N, A):
    rain = [0] * N
    for i in range(N):
        if i == 0:
            rain[0] = A[0] - A[N-1] / 2 - A[1] / 2
        elif i == N-1:
            rain[N-1] = A[N-1] - A[N-2] / 2 - A[0] / 2
        else:
            rain[i] = A[i] - A[i-1] / 2 - A[i+1] / 2
    return rain

N = int(input())
A = list(map(int, input().split()))
print(*compute_rainfall(N, A))

=======
Suggestion 10

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += arr[i]
    result = []
    for i in range(n):
        result.append(sum - arr[i])
    print(' '.join(map(str, result)))
