Synthesizing 10/10 solutions (Duplicates hidden)

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
    ans = 0
    for i in range(1, n):
        if a[i] == 1:
            ans += 1
        elif a[i] - a[i - 1] == 1:
            continue
        else:
            print(-1)
            return
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(-1)
    else:
        print(n-ans)

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] == i+1:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(N-ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i+1:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(N-ans)

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
    else:
        if a[0] == 1:
            count = 0
            for i in range(1, N):
                if a[i] == a[i-1] + 1:
                    count += 1
                else:
                    break
            print(N - count - 1)
        else:
            print(-1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    broken = 0
    for i in range(n):
        if a[i] == i+1:
            broken += 1
    if broken == n:
        print(-1)
    else:
        print(n - broken)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if 1 not in a:
        print(-1)
    else:
        count = 0
        for i in range(N):
            if a[i] == count + 1:
                count += 1
        print(N - count)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # 1からNまでの整数がそれぞれ何個あるか数える
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1

    # 1からNまでの整数がそれぞれ何個あるか数えた結果、
    # 1からNまでの整数が1個ずつあるものを数える
    ans = 0
    for i in range(1, N + 1):
        if cnt[i] == 1:
            ans += 1

    # 1からNまでの整数が1個ずつあるものの個数を答える
    if ans == 0:
        print(-1)
    else:
        print(ans)

=======
Suggestion 9

def get_int():
    return int(input())
