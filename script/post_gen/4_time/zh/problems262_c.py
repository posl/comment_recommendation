Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a
    ans = 0
    for i in range(1,n+1):
        if a[i] == i:
            for j in range(i+1,n+1):
                if a[j] == j:
                    ans += 1
        else:
            if a[a[i]] == i:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for j in range(1, N + 1):
        i = A[j - 1]
        if i >= j:
            continue
        if A[i - 1] == j:
            ans += 1
    print(ans)

=======
Suggestion 3

def get_count(N, a):
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if min(a[i], a[j]) == i+1 and max(a[i], a[j]) == j+1:
                count += 1
    return count

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(a)

=======
Suggestion 5

def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if A[i] < i + 1:
            continue
        for j in range(i + 1, N):
            if A[j] < i + 1:
                continue
            if A[i] == j + 1 and A[j] == i + 1:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (n + 1)
    for i in range(n):
        l[a[i]] = i
    r = [0] * (n + 1)
    for i in range(n):
        r[a[i]] = i
    ans = 0
    for i in range(1, n + 1):
        ans += (l[i] - l[i - 1]) * (r[i] - r[i - 1])
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[a[i]] = i + 1
    ans = 0
    for i in range(1, n + 1):
        if b[i] == i:
            ans += 1
    for i in range(1, n + 1):
        if b[i] != i:
            if b[b[i]] == i:
                ans += 1
    print(ans)

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def min(a, b):
    if a < b:
        return a
    else:
        return b

=======
Suggestion 10

def solve():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for i in range(N):
        if A[i] <= i + 1:
            continue
        for j in range(i + 1, N):
            if A[j] < A[i]:
                ans += 1
    print(ans)
