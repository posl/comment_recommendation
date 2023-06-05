Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    b = a[n // 2]
    ans = sum(abs(a[i] - b) for i in range(n))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 1:
        ans = 0
        for i in range(n):
            ans += abs(b[i] - b[n // 2])
        print(ans)
    else:
        ans1 = 0
        for i in range(n):
            ans1 += abs(b[i] - b[n // 2])
        ans2 = 0
        for i in range(n):
            ans2 += abs(b[i] - b[n // 2 - 1])
        print(min(ans1, ans2))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    b = a[n // 2]
    print(sum([abs(x - b) for x in a]))

=======
Suggestion 4

def get_min_sadness(n, a):
    min_sadness = 1000000000000000000000000
    for b in range(-100, 101):
        sadness = 0
        for i in range(n):
            sadness += abs(a[i] - (b + i + 1))
        min_sadness = min(min_sadness, sadness)
    return min_sadness

n = int(input())
a = list(map(int, input().split()))
print(get_min_sadness(n, a))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i]-(i+1) for i in range(n)]
    a.sort()
    b = a[n//2]
    print(sum([abs(a[i]-b) for i in range(n)]))

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i]-(i+1) for i in range(n)]
    a.sort()
    b = a[n//2]
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b)
    print(ans)

solve()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [2,2,3,5,5]
    # A = [1,2,3,4,5,6,7,8,9]
    # A = [6,5,4,3,2,1]
    # A = [1,1,1,1,2,3,4]
    # A = [1,1,1,1,1,1,1]
    # A = [1,2,3,4,5,6,7,8,9]
    # A = [1,2,3,4,5,6,7,8,9,10]
    # A = [1,2,3,4,5,6,7,8,9,10,11]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    # A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    # A = [2,2,3,5,5]
    # A = [1,2,3

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = [a[i] - (i + 1) for i in range(n)]
    a.sort()
    b = a[n // 2]
    print(sum(abs(a[i] - b) for i in range(n)))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i] - (i+1)
    sum = abs(sum)
    print(sum)

=======
Suggestion 10

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(n)]
    A.sort()
    b = A[n // 2]
    print(sum(abs(a - b) for a in A))
