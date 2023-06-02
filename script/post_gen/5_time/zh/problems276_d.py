Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    while True:
        if all(i%2==0 for i in a):
            a = [i//2 for i in a]
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        if all([i % 2 == 0 for i in a]):
            a = [i // 2 for i in a]
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all([i % 2 == 0 for i in a]):
            a = [i // 2 for i in a]
            ans += 1
        else:
            break
    while True:
        if all([i % 3 == 0 for i in a]):
            a = [i // 3 for i in a]
            ans += 1
        else:
            break
    if all([i == a[0] for i in a]):
        print(ans)
    else:
        print(-1)

=======
Suggestion 4

def f(a):
    if a % 2 == 0:
        return a // 2
    if a % 3 == 0:
        return a // 3
    return -1

n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    for i in range(n):
        if a[i] % 2 == 1:
            print(ans)
            exit()
        a[i] = f(a[i])
    ans += 1

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        even = 0
        for i in range(N):
            if A[i] % 2 == 1:
                break
            else:
                even += 1
        if even == N:
            ans += 1
            for i in range(N):
                A[i] //= 2
        else:
            break
    print(ans)

=======
Suggestion 6

def f(n):
    if n % 2 == 0:
        return n/2
    elif n % 3 == 0:
        return n/3
    else:
        return -1

N = int(input())
A = list(map(int,input().split()))
count = 0
while True:
    for i in range(N):
        if f(A[i]) != -1:
            A[i] = f(A[i])
        else:
            break
    else:
        count += 1
    if i != N-1:
        break
print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(i % 2 == 0 for i in a):
            a = [i / 2 for i in a]
            count += 1
        elif all(i % 3 == 0 for i in a):
            a = [i / 3 for i in a]
            count += 1
        elif all(i % 2 != 0 for i in a) and all(i % 3 != 0 for i in a):
            break
        else:
            count = -1
            break
    print(count)

=======
Suggestion 8

def solve(n, a):
    ans = 0
    while True:
        flag = False
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                flag = True
                ans += 1
                break
        if not flag:
            break
    return ans

=======
Suggestion 9

def solve(n, a):
    ans = 0
    while True:
        ok = True
        for i in range(n):
            if a[i] % 2 == 1:
                ok = False
        if not ok:
            break
        for i in range(n):
            a[i] = a[i] // 2
        ans += 1
    return ans

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    while True:
        is_even = True
        for i in range(N):
            if A[i] % 2 != 0:
                is_even = False
                break
        if is_even:
            for i in range(N):
                A[i] = A[i] // 2
            count += 1
        else:
            break
    while True:
        is_multiple_of_three = True
        for i in range(N):
            if A[i] % 3 != 0:
                is_multiple_of_three = False
                break
        if is_multiple_of_three:
            for i in range(N):
                A[i] = A[i] // 3
            count += 1
        else:
            break
    for i in range(N):
        if A[i] != 1:
            count = -1
            break
    print(count)
