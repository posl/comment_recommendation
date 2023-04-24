Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            print(a[i-1]+1)
            return
    print(a[n-1]+1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i:
            print(i)
            return
    print(n)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] == ans:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 0:
        print(0)
        return
    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            print(A[i] + 1)
            return
    print(A[-1] + 1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if a[0] != 0:
        print(0)
        return

    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(a[i] + 1)
            return

    print(a[n-1] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] > 0:
        print(0)
        return
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            print(A[i]+1)
            return
    print(A[-1]+1)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return

    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(a[i]+1)
            return

    print(a[-1]+1)

=======
Suggestion 8

def problem245_b():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print(a[i - 1] + 1)
            return
    print(a[n - 1] + 1)

=======
Suggestion 9

def solve():
    N = int(input())
    A = [int(a) for a in input().split()]
    A.sort()
    for i in range(N):
        if i != A[i]:
            return i
    return N

=======
Suggestion 10

def find_missing_number(numbers):
    numbers.sort()
    if numbers[0] != 0:
        return 0
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] > 1:
            return numbers[i - 1] + 1
    return numbers[-1] + 1

n = int(input())
numbers = list(map(int, input().split()))
print(find_missing_number(numbers))
