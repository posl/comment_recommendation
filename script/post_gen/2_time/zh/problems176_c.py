Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] - a[0]
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += max(a[i]-i, 0)
    print(ans)
solve()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
    max_a = 0
    ans = 0
    for i in range(n):
        if a[i] > max_a:
            max_a = a[i]
        else:
            ans += max_a - a[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] - a[i - 1] > 1:
            print(-1)
            return
        elif a[i] - a[i - 1] == 1:
            ans += 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 0
    for i in range(1, n):
        if a[i-1] < a[i]:
            b[i] = b[i-1] + 1
        else:
            b[i] = 0
    print(sum(b))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(a[i] - i - 1)
    b.sort()
    if n % 2 == 1:
        k = b[n // 2]
    else:
        k = (b[n // 2] + b[n // 2 - 1]) // 2
    ans = 0
    for i in range(n):
        ans += abs(b[i] - k)
    print(ans)

=======
Suggestion 7

def solve(N, A):
    A = sorted(A)
    ans = 0
    for i in range(N):
        ans += A[i] - A[0]
    return ans

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - A[i - 1])
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(A[0])
        exit()
    if N == 2:
        print(max(A[0], A[1]))
        exit()
    max_h = 0
    for i in range(N):
        max_h = max(max_h, A[i])
        if i > 0:
            if A[i] > A[i - 1]:
                A[i] = A[i - 1]
    print(max_h)
main()

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 从后往前遍历，最后一个人的高度是A[-1]，那么他前面的人的高度必须是A[-1]或者A[-1]-1
    # 因为我们要找最小的凳子总高度，所以我们取A[-1]和A[-1]-1中最小的那个
    # 然后往前遍历，每个人的高度必须是他前面的人的高度或者比他前面的人的高度小1
    # 我们每次都取这两个数中较小的那个，直到遍历完所有的人
    # 最后的结果就是我们要找的答案

    # 这里我们使用min()函数来找两个数中较小的那个
    # min()函数的使用方法是min(x, y)，它会返回x和y中较小的那个数
    # 例如min(2, 3)会返回2，min(5, 3)会返回3
    # 这里我们使用min()函数来找两个数中较小的那个
    # min()函数的使用方法是min(x, y)，它会返回x和y中较小的那个数
    # 例如min(2, 3)会返回2，min(5, 3)会返回3

    # 我们从后往前遍历，最后一个人的高度是A[-1]，那么他前面的人的高度必须是A[-1]或者A[-1]-1
    # 因为我们要找最小的凳子总高度，所以我们取A[-1]和A[-1]-1中最小的那个
    # 然后往前遍历，每个人的高度必须是他前面的人的高度或者比他前面的人的
