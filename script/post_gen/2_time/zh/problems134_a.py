Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    total = sum(A)
    for i in range(N):
        print(total - A[i], end=' ')
    print()

=======
Suggestion 2

def solve(N, A):
    ans = [0] * N
    for i in range(N):
        ans[i] = A[i] * 2
    for i in range(N):
        ans[i] -= sum(ans) / 2
    return ans

N = int(input())
A = list(map(int, input().split()))
print(*solve(N, A))

=======
Suggestion 3

def rain(N, A):
    # 计算每座山收到的雨量
    # 思路：计算每个山的雨水量，然后用总雨水量减去每个山的雨水量
    # 从第一个山开始，计算雨水量，然后累加雨水量，直到最后一个山
    # 然后从第二个山开始，计算雨水量，然后累加雨水量，直到最后一个山
    # 依次类推，直到最后一个山
    # 最后计算总雨水量减去每个山的雨水量，就是每个山收到的雨水量
    # 注意：最后一个山的雨水量要用第一个山的雨水量减去最后一个山的雨水量
    # 注意：第一个山的雨水量要用最后一个山的雨水量减去第一个山的雨水量
    # 雨水量 = (前一个山的雨水量 + 后一个山的雨水量) / 2
    # 从第一个山开始，计算雨水量，然后累加雨水量，直到最后一个山
    # 然后从第二个山开始，计算雨水量，然后累加雨水量，直到最后一个山
    # 依次类推，直到最后一个山
    # 最后计算总雨水量减去每个山的雨水量，就是每个山收到的雨水量
    # 注意：最后一个山的雨水量要用第一个山的雨水量减去最后一个山的雨水量
    # 注意：第一个山的雨水量要用最后一个山的雨水量减去第一个山的雨水量
    # 雨水量 = (前一个山的雨水量 + 后一个山的

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*n
    ans[0] = sum(a[1::2]) - sum(a[0::2])
    for i in range(1, n):
        ans[i] = 2*a[i-1] - ans[i-1]
    print(*ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(1, N):
        ans[i] = 2 * A[i - 1] - ans[i - 1]
    ans[0] = 2 * A[N - 1] - ans[N - 1]
    print(*ans)

=======
Suggestion 6

def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - b[i - 1] // 2 - b[(i + 1) % n] // 2
    print(*b)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - sum(B)
    print(*B)

solve()

=======
Suggestion 8

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
        B[i] = 2 * A[i - 1] - B[i - 1]
    print(*B)

=======
Suggestion 9

def solve(n, a):
    # print(n, a)
    # print(a[0], a[1], a[2])
    b = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            b[i] = a[i] - (a[i+1] + a[n-1]) // 2
        elif i == n-1:
            b[i] = a[i] - (a[0] + a[i-1]) // 2
        else:
            b[i] = a[i] - (a[i+1] + a[i-1]) // 2
    return b

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - sum(B) * 2
    print(*B)
