Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit()
    ans = 1
    for i in a:
        ans *= i
        if ans > 10**18:
            print(-1)
            exit()
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    result = 1
    for a in A:
        result *= a
        if result > 10**18:
            print(-1)
            return
    print(result)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit()
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            exit()
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        return 0
    ans = 1
    for a in A:
        ans *= a
        if ans > 10 ** 18:
            return -1
    return ans

print(solve())

=======
Suggestion 5

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
Suggestion 6

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

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
        return
    x = 1
    for a in A:
        x *= a
        if x > 10**18:
            print(-1)
            return
    print(x)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        print(0)
    else:
        prod = 1
        for i in range(N):
            prod *= A[i]
            if prod > 10 ** 18:
                print(-1)
                exit()
        print(prod)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in a:
        ans *= i
    if ans > 10**18:
        print(-1)
    else:
        print(ans)

=======
Suggestion 10

def problems169_b():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        exit()
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            exit()
    print(ans)
    return

problems169_b()
