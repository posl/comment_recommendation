Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_comfort(n, a):
    c = [0 for i in range(n)]
    c[0] = a[0]
    for i in range(1, n):
        c[i] = min(c[i-1], a[i])
    s = sum(a)
    for i in range(1, n):
        s += min(a[i-1], a[i])
    return s - max(c)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    tmp = 0
    for i in range(N):
        tmp += A[i]
    ans = tmp
    for i in range(N):
        tmp += A[i+N] - A[i]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    ans -= max(A)
    print(ans)

=======
Suggestion 4

def get_max_comfort(n, list):
    # 1. get the max comfort for the first player
    comfort = 0
    for i in range(1, n):
        comfort += min(list[i-1], list[i])
    comfort += min(list[n-1], list[0])

    # 2. get the max comfort for the second player
    # 2.1 get the max comfort for the first player
    comfort2 = 0
    for i in range(2, n):
        comfort2 += min(list[i-1], list[i])
    comfort2 += min(list[n-1], list[1])
    comfort2 += min(list[0], list[1])

    # 2.2 get the max comfort for the second player
    comfort3 = 0
    for i in range(2, n):
        comfort3 += min(list[i-2], list[i])
    comfort3 += min(list[n-2], list[0])
    comfort3 += min(list[n-1], list[0])

    # 3. return the max comfort
    return max(comfort, comfort2, comfort3)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a + a
    a.append(0)
    s = sum(a[:n])
    ans = s
    t = s
    for i in range(n):
        t = t + a[i+n] - a[i]
        ans = max(ans, t)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sumA = sum(A)
    sumB = 0
    for i in range(1, N):
        if i % 2 == 1:
            sumB += A[i]
    maxsumB = sumB
    for i in range(N):
        if i % 2 == 0:
            sumB += A[i]
        else:
            sumB -= A[i]
        maxsumB = max(maxsumB, sumB)
    print(sumA - maxsumB)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i // 2]
    print(ans)

solve()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    result = 0
    for i in range(1, N):
        result += A[i // 2]
    print(result)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    for i in range(N):
        ans += A[i]
    if N == 2:
        print(ans)
        return
    s = 0
    for i in range(N):
        s += A[i]
    t = s
    for i in range(N, 2*N):
        s += A[i]
        s -= A[i-N]
        if s < t:
            t = s
    print(ans - t)

solve()

=======
Suggestion 10

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = A + A
    sum = 0
    for i in range(N):
        sum += A[i]
    max = sum
    for i in range(N):
        sum -= A[i]
        sum += A[i+N//2]
        if sum > max:
            max = sum
    print(max)
