Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
        while a[i] % 3 == 0:
            a[i] = a[i] / 3
            count += 1
    if len(set(a)) == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i]%2 == 0:
            ans += 1
            a[i] /= 2
        while a[i]%3 == 0:
            ans += 1
            a[i] /= 3
    if all(a[i] == a[0] for i in range(n)):
        print(ans)
    else:
        print(-1)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
            else:
                print(cnt)
                exit()
        cnt += 1

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1

        while a[i] % 3 == 0:
            a[i] /= 3
            count += 1

    if len(set(a)) == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                ans += 1
                flag = False
                break
        if flag:
            break
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while all(i % 2 == 0 for i in a):
        a = [i / 2 for i in a]
        cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            cnt += 1
            continue
        break
    if all(a == A[0] for a in A):
        print(cnt)
    else:
        print(-1)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 1:
                print(cnt)
                exit()
            a[i] = a[i] // 2
        cnt += 1

=======
Suggestion 9

def div2(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count

=======
Suggestion 10

def div_2(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count
