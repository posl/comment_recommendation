Synthesizing 10/10 solutions

=======
Suggestion 1

def div_num(n):
    count=0
    while n%2==0:
        n=n//2
        count+=1
    return count

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] = A[i] / 2
            count += 1
        while A[i] % 3 == 0:
            A[i] = A[i] / 3
            count += 1
    if len(set(A)) == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
        while a[i] % 3 == 0:
            a[i] //= 3
            ans += 1
    if len(set(a)) == 1:
        print(ans)
    else:
        print(-1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] // 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)

=======
Suggestion 6

def solve(N, A):
    cnt = 0
    while True:
        flg = True
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            elif A[i] % 3 == 0:
                A[i] //= 3
            else:
                flg = False
                break
        if flg:
            cnt += 1
        else:
            break
    if all([a == A[0] for a in A]):
        return cnt
    else:
        return -1

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                print(cnt)
                return
        cnt += 1

        if cnt > 100:
            print(-1)
            return

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            else:
                break
        else:
            count += 1
            continue

        break

    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = 0
    while True:
        if all(a % 2 == 0 for a in A):
            A = [a / 2 for a in A]
            count += 1
        else:
            break

    print(count)

=======
Suggestion 10

def solve(n, a):
    count = 0
    while True:
        i = 0
        for j in a:
            if j % 2 == 0:
                i += 1
        if i == n:
            count += 1
            for j in range(n):
                a[j] = a[j] // 2
        else:
            break
    while True:
        i = 0
        for j in a:
            if j % 3 == 0:
                i += 1
        if i == n:
            count += 1
            for j in range(n):
                a[j] = a[j] // 3
        else:
            break
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            return -1
    return count
