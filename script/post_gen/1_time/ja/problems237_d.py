Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()

    A = [0]
    for i in range(1, N+1):
        if S[i-1] == 'L':
            A.insert(0, i)
        else:
            A.append(i)

    print(" ".join(map(str, A)))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i]=='L':
            A.insert(0,i+1)
        else:
            A.append(i+1)
    print(*A)
main()

=======
Suggestion 3

def solve():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N+1):
        if S[i-1] == "L":
            A.insert(0, i)
        else:
            A.append(i)
    print(*A)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    L = 0
    R = 0
    for i in range(N):
        if S[i] == 'L':
            L += 1
        else:
            R += 1
    A = [0] * (N + 1)
    if L == 0:
        for i in range(N):
            A[i + 1] = i + 1
    elif R == 0:
        for i in range(N):
            A[i] = N - i
    else:
        for i in range(N):
            if S[i] == 'L':
                A[i + 1 - L] = i + 1
            else:
                A[i + R + 1] = i + 1
    print(*A[1:])

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0] * (n+1)
    l = 0
    r = n
    for i in range(n):
        if s[i] == 'L':
            a[r] = i+1
            r -= 1
        else:
            a[l] = i+1
            l += 1
    print(*a)

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1, n):
        if s[i-1] == 'L':
            a.insert(0, i)
        else:
            a.append(i)
    print(*a)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.append(i+1)
        else:
            a.insert(-1,i+1)
    print(*a)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    l = 0
    r = n-1
    ans = [0 for i in range(n)]
    for i in range(n):
        if s[i] == "L":
            ans[r] = i+1
            r -= 1
        else:
            ans[l] = i+1
            l += 1
    print(*ans)

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.readline

    n = int(readline())
    s = readline().rstrip()

    ans = []
    l = 0
    r = n
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            ans.append(r)
            r -= 1
        else:
            ans.append(l)
            l += 1
    print(*ans[::-1])

=======
Suggestion 10

def main():
    N = int(input())
    S = input()

    #A = [0 for i in range(N+1)]
    A = [0] * (N+1) # こっちの書き方の方が早い
    l = 0
    r = N

    for i in range(N):
        if S[i] == 'L':
            A[l] = i+1
            l += 1
        else:
            A[r] = i+1
            r -= 1

    print(*A)
