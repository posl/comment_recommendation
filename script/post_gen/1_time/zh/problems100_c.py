Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while True:
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
                count += 1
            else:
                break
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 3

def problem100_c():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        tmp = a[i]
        while tmp % 2 == 0:
            tmp //= 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i]%2 == 0:
            a[i] = a[i] // 2
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                print(count)
                return
        count += 1

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            count += 1
    print(count)

=======
Suggestion 8

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            ans += 1
    print(ans)

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)
