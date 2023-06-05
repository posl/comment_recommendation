Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_max = max(a)
    a_min = min(a)
    b_max = max(b)
    b_min = min(b)

    if (a_max - a_min) > k or (b_max - b_min) > k:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = max(a[0], b[0])
    r = min(a[0] + k, b[0] + k)
    for i in range(1, n):
        l = max(l, a[i], b[i])
        r = min(r, a[i] + k, b[i] + k)
        if l > r:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = 0
    for i in range(n):
        diff += abs(a[i] - b[i])
    if diff > k:
        print('No')
    else:
        if (k - diff) % 2 == 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = 0
    for i in range(n):
        diff += abs(a[i] - b[i])
    if diff > k:
        print("No")
    else:
        if (k - diff) % 2 == 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def check(N, K, A, B):
    for i in range(N):
        if abs(A[i]-B[i]) > K:
            return False
    return True

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

=======
Suggestion 8

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    while A:
        if abs(A.pop() - B.pop()) > K:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 检查是否有解
    a.sort()
    b.sort()
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            print("No")
            return
    print("Yes")
