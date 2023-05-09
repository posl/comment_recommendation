Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            ans += 1
            a[i] /= 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
    print(ans)
    return

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count = count + 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
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
            a[i] /= 2
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        c = 0
        while a[i] % 2 == 0:
            a[i] /= 2
            c += 1
        count += c
    print(count)

=======
Suggestion 7

def main() :
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n) :
        while a[i] % 2 == 0 :
            ans += 1
            a[i] //= 2
    print(ans)

=======
Suggestion 8

def divide2(n):
    if n%2 == 0:
        return n/2
    else:
        return 0

=======
Suggestion 9

def divide2(x):
    return x/2
