Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 4

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
                return
        print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    ans = 1
    for a in A:
        ans *= a
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)
    return

=======
Suggestion 6

def solve(n, a):
    if 0 in a:
        return 0
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            return -1
    return ans

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in a:
            ans *= i
            if ans > 10**18:
                print(-1)
                return
        print(ans)
