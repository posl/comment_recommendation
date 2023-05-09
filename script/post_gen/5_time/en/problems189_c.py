Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for l in range(n):
        x = a[l]
        for r in range(l, n):
            x = min(x, a[r])
            ans = max(ans, x * (r - l + 1))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_oranges = 0
    for l in range(N):
        for r in range(l, N):
            for x in range(1, 10000):
                oranges = 0
                for i in range(l, r+1):
                    if A[i] >= x:
                        oranges += x
                if oranges > max_oranges:
                    max_oranges = oranges
    print(max_oranges)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_orange = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j]+1):
                orange = 0
                for l in range(i, j+1):
                    if a[l] >= k:
                        orange += k
                if orange > max_orange:
                    max_orange = orange
    print(max_orange)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(1, a[j]+1):
                if k > max and min(a[i:j+1]) >= k:
                    max = k
    print(max)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))

    max_oranges = 0
    for l in range(n):
        for r in range(l, n):
            for x in range(1, max(a[l:r+1])+1):
                oranges = x * (r - l + 1)
                if oranges > max_oranges:
                    max_oranges = oranges
    print(max_oranges)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    max_oranges = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(1, A[j]+1):
                oranges = 0
                for l in range(i, j+1):
                    if A[l] >= k:
                        oranges += k
                if oranges > max_oranges:
                    max_oranges = oranges

    print(max_oranges)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_orange = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(1, A[j]+1):
                if max_orange < sum(A[i:j+1]) - k*(j-i+1):
                    max_orange = sum(A[i:j+1]) - k*(j-i+1)
    print(max_orange)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_index = a.index(max_a)
    a.pop(max_index)
    print(max_a * (n - 1) + sum(a))
