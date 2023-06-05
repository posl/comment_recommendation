Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_even_sum(A):
    A = sorted(A)
    max_even = -1
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] + A[j]) % 2 == 0:
                max_even = max(max_even, A[i] + A[j])
    return max_even

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0:
        print(-1)
        return
    if n == 2:
        if a[0] == a[1]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 3:
        if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 4:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[1] == a[2] or a[1] == a[3] or a[2] == a[3]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 5:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[0] == a[4] or a[1] == a[2] or a[1] == a[3] or a[1] == a[4] or a[2] == a[3] or a[2] == a[4] or a[3] == a[4]:
            print(-1)
            return
        else:
            print(a[0]+a[1])
            return
    if n == 6:
        if a[0] == a[1] or a[0] == a[2] or a[0] == a[3] or a[0] == a[4] or a[0] == a[5] or a[1] == a[2] or a[1] == a[3] or a[1] == a[4] or a[1] == a[5] or a[2] == a[3] or a[2] == a[4] or a[2] == a[5] or a[

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0:
        print(a[0])
    else:
        for i in range(n):
            if a[i] % 2 == 0:
                print(a[i])
                break
            else:
                if i == n - 1:
                    print(-1)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
        return
    for i in range(n-1):
        if a[i] % 2 == 0:
            print(a[i])
            return
    print(-1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[-1] % 2 == 1:
        print(-1)
        return
    
    for i in range(n):
        if a[i] % 2 == 1:
            continue
        if a[i] * 2 == a[-1]:
            continue
        if a[i] * 2 in a:
            print(a[-1])
            return
    print(-1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    max_a = max(a)
    for i in range(max_a+1):
        if i%2==0 and i//2 in a:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def solve(n, a):
    a.sort()
    for i in range(n - 1, 0, -1):
        if a[i] == a[i - 1]:
            return a[i] * 2
    return -1

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n):
        for j in range(i+1, n):
            if (a[i] + a[j]) % 2 == 0:
                print(a[i] + a[j])
                return
    print(-1)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        for i in range(n-1):
            if a[i] % 2 == 0:
                print(a[i])
                break
        else:
            print(-1)
