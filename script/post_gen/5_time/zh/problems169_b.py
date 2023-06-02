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
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    if 0 in A:
        print(0)
        return
    for i in A:
        ans *= i
        if ans > 10 ** 18:
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
    result = 1
    for i in range(n):
        result *= a[i]
        if result > 10**18:
            print(-1)
            return
    print(result)
    return

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in a:
        ans *= i
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    res = 1
    for i in range(n):
        res *= a[i]
        if res > 10**18:
            print(-1)
            return
    print(res)

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit(0)
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            exit(0)
    print(ans)
