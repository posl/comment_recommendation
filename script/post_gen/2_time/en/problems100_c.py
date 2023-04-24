Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            count += 1
    print(count)

main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                print(count)
                return
        count += 1

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while all(a % 2 == 0 for a in A):
        A = [a / 2 for a in A]
        count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        while a[i]%2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    # import sys
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            count += 1
            a[i] /= 2
    print(count)
