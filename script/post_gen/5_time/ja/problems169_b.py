Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    N = int(input())
    As = list(map(int, input().split()))

    # compute
    if 0 in As:
        print(0)
        exit()
    ans = 1
    for A in As:
        ans *= A
        if ans > 10**18:
            print(-1)
            exit()

    # output
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
    N = int(input())
    A = list(map(int, input().split()))
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
Suggestion 4

def main():
    # input
    N = int(input())
    A_list = list(map(int, input().split()))

    # compute
    A = 1
    for i in range(N):
        A *= A_list[i]

    # output
    if A > 10**18:
        print(-1)
    else:
        print(A)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit()
    p = 1
    for i in a:
        p *= i
        if p > 10**18:
            print(-1)
            exit()
    print(p)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    if 0 in A:
        ans = 0
    else:
        for a in A:
            ans *= a
            if ans > 10**18:
                ans = -1
                break
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            ans = -1
            break
    print(ans)
