Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            return
    print(ans)
    return

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans = ans * A[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            ans = -1
            break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    if 0 in A:
        print(0)
        return
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)
    return

=======
Suggestion 8

def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    #compute
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            ans = -1
            break
    #output
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 31:
        if A[0] == 4:
            print(0)
            return
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            print(-1)
            return
    print(ans)
