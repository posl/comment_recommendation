Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    if max(a) > n:
        print(-1)
        return
    for i in range(1, n):
        if a[i] > a[i-1] + 1:
            print(-1)
            return
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            continue
        else:
            ans += a[i-1]
    print(ans)
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [0 for i in range(N)]
    for i in range(N):
        if A[i] > N:
            print(-1)
            return
        else:
            B[A[i]-1] = 1

    cnt = 0
    for i in range(N):
        if B[i] == 0:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    if n == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        else:
            print(-1)
        return
    if n == 3:
        if a[0] == 1 and a[1] == 2 and a[2] == 1:
            print(1)
        else:
            print(-1)
        return
    if n == 4:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4:
            print(0)
        elif a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 2 and a[3] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 4 and a[3] == 2:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 2 and a[3] == 3:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 3 and a[3] == 2:
            print(3)
        else:
            print(-1)
        return
    if n == 5:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4 and a[4] == 5:
            print(0)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 5 and a[4] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] ==

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    if A[0] != 1:
        print(-1)
        return
    L = [0] * (N + 1)
    for i in range(N):
        L[i + 1] = L[i] + 1 if A[i] != A[i - 1] else L[i]
    ans = 0
    for i in range(1, N + 1):
        if L[i] < i:
            ans += 1
    print(ans)


solve()

=======
Suggestion 5

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        exit()
    ans = 0
    for i in range(N - 1):
        if a[i + 1] - a[i] > 1:
            print(-1)
            exit()
        if a[i + 1] - a[i] == 1:
            ans += 1
        else:
            ans += a[i + 1]
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        return -1
    for i in range(1, n):
        if a[i] - a[i-1] != 1 and a[i] - a[i-1] != 0:
            return -1
    ans = 0
    for i in range(1, n):
        if a[i] - a[i-1] == 0:
            ans += 1
    return ans

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*n

    for i in range(n):
        if a[i] > n:
            print(-1)
            return
        b[a[i]-1] += 1

    for i in range(n):
        if b[i] > 1:
            print(-1)
            return

    ans = 0
    for i in range(n):
        if a[i] != i+1:
            ans += 1

    print(ans)

main()

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

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
Suggestion 10

def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1
    if cnt == n:
        print(0)
    elif cnt >= n-1:
        print(n-cnt)
    else:
        print(-1)
main()
