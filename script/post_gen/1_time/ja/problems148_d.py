Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] != i+1:
            ans += 1
    if ans > 2:
        print(-1)
    else:
        print(ans)

main()

=======
Suggestion 2

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
    
    i = 1
    ans = 0
    while i < n:
        if a[i] != i + 1:
            ans += 1
        else:
            i += 1
        i += 1
    
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] != 1:
        return -1
    ans = 0
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            return -1
        elif A[i+1] - A[i] == 1:
            ans += 1
        else:
            ans += A[i+1]
    return ans

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i-1] == i:
            ans += 1
            a[i-1] = 0
            a[i] = 0
    if a[N-1] == N:
        ans += 1
    print(N-ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    if a[0] != 1:
        print(-1)
        exit()
    for i in range(n-1):
        if a[i+1] > a[i] + 1:
            print(-1)
            exit()
    ans = 0
    for i in range(n-1):
        if a[i+1] == a[i] + 1:
            ans += 1
    print(n-1-ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if 1 not in a:
        print(-1)
        return
    if a[0] != 1:
        print(-1)
        return
    count = 0
    now = 1
    for i in range(1, N):
        if a[i] == now + 1:
            now += 1
        else:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] > n-1:
            print(-1)
            return
        b[a[i]] += 1
    ans = 0
    for i in range(n):
        if b[i] > i:
            ans += b[i] - i
    print(ans)
    return

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = 0
    for i in range(1, N+1):
        if a[i] == i:
            ans += 1
    if ans == N:
        print(0)
    else:
        print(N-ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        b[A[i] - 1] += 1
    ans = 0
    for i in range(N):
        if b[i] > i + 1:
            ans += b[i] - (i + 1)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if max(a) > n:
        print("-1")
        return
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    print(n - max(b))
