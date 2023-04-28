Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] != i + 1:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        if A[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if max(A) == N:
        print(-1)
        return
    ans = 0
    for i in range(N-1):
        if A[i] == i+1:
            ans += 1
        else:
            break
    print(N-ans)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
    if ans == N:
        print(0)
    elif ans == N - 1:
        print(1)
    else:
        print(N - ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    b = [0] * n
    for i in range(n):
        if a[i] >= 0:
            b[a[i]] += 1
    c = []
    for i in range(n):
        if b[i] == 0:
            c.append(i)
    if len(c) == 0:
        print(-1)
        return
    ans = 0
    for i in range(n):
        if b[i] > 1:
            for j in range(b[i] - 1):
                if len(c) == 0:
                    print(-1)
                    return
                k = c.pop()
                a[k] = i
                ans += 1
    for i in range(n):
        if a[i] < 0:
            a[i] = c.pop()
    print(ans)
    return

main()

=======
Suggestion 5

def problems148_d():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] == ans + 1:
            ans += 1
    if ans == 0:
        print(-1)
    else:
        print(n - ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] > n - 1:
            print(-1)
            return
        b[a[i]] += 1
    ans = 0
    for i in range(n):
        if b[i] > i:
            ans += b[i] - i
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if A[0] != 1:
        return -1

    for i in range(1, N):
        if A[i] != A[i - 1] + 1:
            return -1

    return N - 1

print(solve())

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    ans = 0
    for i in range(1, N + 1):
        if A[i] != i:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def problem148_d():
    N = int(input())
    A = list(map(int, input().split()))

    if A[0] != 1:
        return -1

    for i in range(1, N):
        if A[i] - A[i-1] > 1:
            return -1

    ans = 0
    for i in range(N-1, 0, -1):
        if A[i] == A[i-1] + 1:
            ans += 1
        else:
            ans += A[i]
    return ans

print(problem148_d())

=======
Suggestion 10

def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    ans = -1
    if a_list[0] == 1 and a_list[-1] == 1:
        ans = 0
        for i in range(1, N):
            if a_list[i] - a_list[i-1] > 1:
                ans = -1
                break
            elif a_list[i] - a_list[i-1] == 1:
                ans += 1
    print(ans)
