Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        if a[i-1] > a[i]:
            ans += a[i-1] - a[i]
            a[i-1] = a[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    h = 0
    for i in range(n-1, -1, -1):
        if a[i] > h:
            h = a[i]
        elif a[i] < h:
            h = a[i] = h
    print(sum(a))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_height = 0
    stools = 0
    for i in range(n):
        if a[i] >= max_height:
            stools += a[i] - max_height
            max_height = a[i]
        else:
            max_height = a[i]
    print(stools)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min_height = 0
    for i in range(N):
        if A[i] > min_height + 1:
            print(-1)
            return
        elif A[i] == min_height + 1:
            min_height += 1
    print(N - min_height)
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    stools = [0] * N
    stools[0] = A[0]
    for i in range(1, N):
        if A[i] <= stools[i-1]:
            stools[i] = A[i]
        else:
            stools[i] = stools[i-1]
    print(sum(stools))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    sum = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            sum += a[i] - a[i-1]
            a[i] = a[i-1]
    print(sum)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    h = 0
    for i in range(N):
        if A[i] > h + 1:
            print(-1)
            return
        elif A[i] == h + 1:
            h += 1
    print(sum(A))
solve()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    count = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            count += A[i] - A[i+1]
            A[i+1] = A[i]
    print(count)
    return

=======
Suggestion 9

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - i - 1
    b.sort()
    return b[n // 2] + sum(abs(b[i] - b[n // 2]) for i in range(n))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    #print(a)
    h = 0
    for i in range(n):
        if h < a[i]:
            h = a[i]
        else:
            if a[i] > 0:
                h = (a[i] // h + 1) * h
    print(h)

main()
