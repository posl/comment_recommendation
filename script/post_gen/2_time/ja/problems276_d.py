Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] /= 2
            elif A[i] % 3 == 0:
                A[i] /= 3
            else:
                break
        else:
            count += 1
            continue
        break
    if A.count(A[0]) == N:
        print(count)
    else:
        print(-1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] = A[i] / 2
            elif A[i] % 3 == 0:
                A[i] = A[i] / 3
            else:
                print(-1)
                return
        if len(set(A)) == 1:
            print(count)
            return
        else:
            count += 1

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
            else:
                if A.count(A[i]) == N:
                    print(cnt)
                    return
                else:
                    print(-1)
                    return
        cnt += 1

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] /= 2
            elif a[i] % 3 == 0:
                a[i] /= 3
            else:
                print(-1)
                return
        if len(set(a)) == 1:
            print(ans)
            return
        ans += 1

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        while a % 2 == 0 or a % 3 == 0:
            if a % 2 == 0:
                a //= 2
                ans += 1
            elif a % 3 == 0:
                a //= 3
                ans += 1
    for a in A:
        if a != A[0]:
            ans = -1
            break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        if all([a % 2 == 0 for a in A]):
            A = [a // 2 for a in A]
            ans += 1
        else:
            break
    if all([a == A[0] for a in A]):
        print(ans)
    else:
        print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                print(ans)
                return

        A = [a//2 for a in A]
        ans += 1

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

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

    if A == [1] * N:
        print(count)
    else:
        print(-1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != A[-1]:
        print(-1)
        return
    two = 0
    three = 0
    for a in A:
        while a % 2 == 0:
            a //= 2
            two += 1
        while a % 3 == 0:
            a //= 3
            three += 1
    if a != 1:
        print(-1)
        return
    print(two + three)
