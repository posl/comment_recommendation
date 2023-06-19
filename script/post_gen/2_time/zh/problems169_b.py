Synthesizing 10/10 solutions

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
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)
    return

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int,input().split()))
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
Suggestion 4

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    if 0 in a_list:
        print(0)
        return
    ans = 1
    for a in a_list:
        ans *= a
        if ans > 1000000000000000000:
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
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = map(int, input().split())
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
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = 1
    if 0 in A:
        print(0)
    else:
        for a in A:
            result *= a
            if result > 10**18:
                print(-1)
                exit()
        print(result)

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in a:
            ans *= i
            if ans > 10 ** 18:
                print(-1)
                return
        print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
    else:
        ans = 1
        for i in range(n):
            ans *= a[i]
            if ans > 10**18:
                print(-1)
                exit()
        print(ans)
