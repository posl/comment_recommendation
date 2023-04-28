Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        ok = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                ans += 1
                ok = False
                break
        if ok:
            break
    while True:
        ok = True
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] //= 3
                ans += 1
                ok = False
                break
        if ok:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while 1:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                count = -1
                break
        if count == -1:
            break
        else:
            count += 1
        if a.count(a[0]) == n:
            break
    print(count)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            ans += 1
            A = [a // 2 for a in A]
        elif any([a % 2 == 0 for a in A]):
            print(ans)
            exit()
        else:
            break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a // 2 for a in A]
            ans += 1
        elif all(a % 3 == 0 for a in A):
            A = [a // 3 for a in A]
            ans += 1
        else:
            break
    if all(a == A[0] for a in A):
        print(ans)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a//2 for a in A]
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        b = [i for i in a if i % 2 == 0]
        if len(b) == len(a):
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    while True:
        c = [i for i in a if i % 3 == 0]
        if len(c) == len(a):
            a = [i // 3 for i in a]
            ans += 1
        else:
            break
    if len(set(a)) == 1:
        print(ans)
    else:
        print(-1)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    c = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a / 2 for a in A]
            c += 1
        elif all(a % 3 == 0 for a in A):
            A = [a / 3 for a in A]
            c += 1
        else:
            break
    if all(a == A[0] for a in A):
        print(c)
    else:
        print(-1)

=======
Suggestion 8

def func(a):
    cnt = 0
    while True:
        for i in range(len(a)):
            if a[i] % 2 == 1:
                return cnt
        a = [i / 2 for i in a]
        cnt += 1

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    while True:
        if all( a[i]%2 == 0 for i in range(n) ):
            a = [a[i]//2 for i in range(n)]
            count += 1
        else:
            break

    while True:
        if all( a[i]%3 == 0 for i in range(n) ):
            a = [a[i]//3 for i in range(n)]
            count += 1
        else:
            break

    if all( a[i] == a[0] for i in range(n) ):
        print(count)
    else:
        print(-1)

=======
Suggestion 10

def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
