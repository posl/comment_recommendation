Synthesizing 10/10 solutions (Duplicates hidden)

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
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
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
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] // 2
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while(a[i] % 2 == 0):
            a[i] = a[i] / 2
            count = count + 1
    print(count)

=======
Suggestion 8

def count_divide_by_2(num):
    count = 0
    while num % 2 == 0:
        num = num // 2
        count += 1
    return count

=======
Suggestion 9

def count_div_by_2(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count
