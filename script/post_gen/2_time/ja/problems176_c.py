Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] < A[i+1]:
            continue
        else:
            ans += A[i] - A[i+1]
            A[i+1] = A[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = 0
    ans = 0
    for i in range(n):
        if a[i] > max_a:
            max_a = a[i]
        ans += max_a - a[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n):
        b[i] = a[i] - i
    b.sort()
    median = b[n//2]
    ans = 0
    for i in range(n):
        ans += abs(b[i] - median)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    h = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            h += 1
        else:
            ans += h*(h+1)//2
            h = 0
    ans += h*(h+1)//2
    print(ans+n)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            continue
        else:
            ans += a[i-1] - a[i] + 1
            a[i] = a[i-1] + 1
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] < a[i+1]:
            continue
        else:
            ans += a[i] - a[i+1]
            a[i+1] = a[i]
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > ans:
            ans += 1
    print(N - ans)
solve()

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    s = [a[0]]
    for i in range(1, n):
        if a[i] < s[-1]:
            s.append(a[i])
        else:
            s.append(s[-1])
    s.reverse()
    ans = 0
    for i in range(n):
        ans += s[i] - a[i]
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A[::-1]
    max_height = 0
    count = 0
    for i in range(N):
        if A[i] > max_height:
            max_height = A[i]
        elif A[i] < max_height:
            count += max_height - A[i]
        else:
            continue
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    result = 0
    for i in range(N):
        if A[i] > A[i+1]:
            result += A[i] - A[i+1]
            A[i] = A[i+1]
    print(result)
