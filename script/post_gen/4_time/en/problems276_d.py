Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            ans += 1
            a[i] //= 2
        while a[i] % 3 == 0:
            ans += 1
            a[i] //= 3
    print(ans if len(set(a)) == 1 else -1)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        while i % 2 == 0:
            i = i // 2
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            else:
                print(ans)
                exit()
        ans += 1

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] / 2
            ans += 1
        while A[i] % 3 == 0:
            A[i] = A[i] / 3
            ans += 1
    for i in range(N):
        if A[i] != A[0]:
            ans = -1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(i%2 == 0 for i in a):
            a = [i/2 for i in a]
            count += 1
        elif all(i%3 == 0 for i in a):
            a = [i/3 for i in a]
            count += 1
        elif all(i%5 == 0 for i in a):
            a = [i/5 for i in a]
            count += 1
        else:
            break
    if all(i==a[0] for i in a):
        print(count)
    else:
        print(-1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    while True:
        if all(a%2==0 for a in A):
            A = [a/2 for a in A]
            cnt += 1
        elif all(a%3==0 for a in A):
            A = [a/3 for a in A]
            cnt += 1
        else:
            break
    if all(a==A[0] for a in A):
        print(cnt)
    else:
        print(-1)

=======
Suggestion 7

def count2(n):
    c = 0
    while n % 2 == 0:
        n = n / 2
        c += 1
    return c

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if sum([i % 2 for i in a]) == 0:
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    while True:
        if sum([i % 3 for i in a]) == 0:
            a = [i // 3 for i in a]
            ans += 1
        else:
            break
    if sum([i % 3 for i in a]) == 0:
        print(ans)
    else:
        print(-1)
solve()

=======
Suggestion 9

def f():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        count += 1
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                return -1
        if len(set(A)) == 1:
            return count

print(f())

=======
Suggestion 10

def d():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all(map(lambda x: x % 2 == 0, a)):
            a = list(map(lambda x: x / 2, a))
            ans += 1
        else:
            break
    print(ans)

d()
