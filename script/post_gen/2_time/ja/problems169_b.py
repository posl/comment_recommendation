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
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= A[i]
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
    if 0 in A:
        print(0)
    else:
        ans = 1
        for a in A:
            ans *= a
            if ans > 10 ** 18:
                print(-1)
                exit()
        print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in a:
        ans *= i
        if ans > 10 ** 18:
            ans = -1
            break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    if 0 in A:
        print(0)
    else:
        ans = 1
        for i in range(N):
            ans *= A[i]
            if ans > 10**18:
                print(-1)
                exit()
        print(ans)
