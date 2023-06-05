Synthesizing 10/10 solutions

=======
Suggestion 1

def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                print(count)
                exit()
        count += 1

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            ans += 1
    print(ans)

=======
Suggestion 5

def get_max_operation_count(n, a):
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                return count
        count += 1

=======
Suggestion 6

def solve(N, A):
    # 除以2的次数
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            ans += 1
    return ans

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i]%2 == 0:
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(i % 2 == 0 for i in a):
            a = [i/2 for i in a]
            count += 1
        else:
            break
    print(count)

=======
Suggestion 9

def function():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                return count
        count += 1

=======
Suggestion 10

def solve(n, a):
    count = 0
    for i in range(n):
        while a[i]%2 == 0:
            a[i] = a[i] / 2
            count += 1
    return count
