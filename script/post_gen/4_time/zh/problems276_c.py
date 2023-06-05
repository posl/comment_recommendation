Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    q = [0] * (n+1)
    for i in range(1, n+1):
        q[p[i]] = i
    print(*q[1:])

=======
Suggestion 2

def find_smaller_permutation(p):
    # 找到下一个最小的排列组合
    # 从右到左找到第一个不是升序的数字
    # 该数字左边的数字都是升序的
    # 从右到左找到第一个比该数字大的数字
    # 交换这两个数字
    # 将该数字右边的数字按升序排列
    # 返回排列组合
    p = list(p)
    for i in range(len(p)-2, -1, -1):
        if p[i] < p[i+1]:
            break
    for j in range(len(p)-1, i, -1):
        if p[j] > p[i]:
            break
    p[i], p[j] = p[j], p[i]
    return p[:i+1] + sorted(p[i+1:])

=======
Suggestion 3

def problem276_c():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

problem276_c()

=======
Suggestion 4

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

=======
Suggestion 5

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

=======
Suggestion 6

def is_sorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(" ".join(map(str, Q)))

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i, p in enumerate(P):
        Q[p-1] = i+1
    print(*Q)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i + 1
    print(" ".join(map(str, q)))
