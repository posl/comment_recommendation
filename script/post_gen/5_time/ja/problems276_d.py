Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all(a%2==0 for a in A):
            A = [a//2 for a in A]
            ans += 1
        elif any(a%2==0 for a in A):
            print(ans)
            return
        else:
            print(ans)
            return

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    cnt = 0
    while True:
        flag = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
                cnt += 1
                flag = False
        if flag:
            break
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0

    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                print(count)
                exit()
        count += 1

    print(-1)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            elif A[i] % 3 == 0:
                A[i] = A[i] // 3
            else:
                break
        else:
            ans += 1
            continue
        break
    if A.count(A[0]) == len(A):
        print(ans)
    else:
        print(-1)

=======
Suggestion 5

def func(n, a):
    cnt = 0
    while True:
        if len(set(a)) == 1 and 1 in set(a):
            return cnt
        if 1 in set(a):
            return -1
        a = [i//2 if i % 2 == 0 else i//3 for i in a]
        cnt += 1

=======
Suggestion 6

def func(n, a):
    cnt = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                break
        else:
            cnt += 1
            continue
        break
    if a.count(a[0]) == n:
        return cnt
    else:
        return -1

n = int(input())
a = list(map(int, input().split()))
print(func(n, a))

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    res = 0
    while all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        res += 1
    print(res)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            A = [a / 2 for a in A]
            count += 1
        elif all([a % 3 == 0 for a in A]):
            A = [a / 3 for a in A]
            count += 1
        else:
            break
    if all([a == A[0] for a in A]):
        print(count)
    else:
        print(-1)

=======
Suggestion 9

def func(a):
    count = 0
    for i in range(len(a)):
        while a[i] % 2 == 0:
            count += 1
            a[i] = a[i] / 2
        while a[i] % 3 == 0:
            count += 1
            a[i] = a[i] / 3
    return count

n = int(input())
a = list(map(int, input().split()))
count = func(a)

=======
Suggestion 10

def cal(a):
    if a % 2 == 0:
        return a / 2
    elif a % 3 == 0:
        return a / 3
    else:
        return -1
