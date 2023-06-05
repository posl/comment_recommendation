Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(len(S)):
        if S[i] == 'L':
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    print(*A)

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            ans.insert(0, i+1)
        else:
            ans.append(i+1)
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
    print(' '.join(map(str, list(range(l+1, 1, -1)) + list(range(l+2, n+1)))))

=======
Suggestion 4

def get_input():
    n = int(input())
    s = input()
    return n, s

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    l = 0
    r = 0
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            l += 1
            ans.insert(l, i+1)
        else:
            r += 1
            ans.insert(l, i+1)
    for i in ans:
        print(i, end=' ')
    print()

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N+1):
        if S[i-1] == 'L':
            A.insert(0, i)
        else:
            A.append(i)
    print(' '.join(map(str, A)))

=======
Suggestion 7

def problems237_d():
    pass

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(' '.join(map(str, A)))

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N):
        if S[i-1] == 'L':
            A.insert(0, i)
        else:
            A.append(i)
    for i in range(N):
        print(A[i], end=' ')
    print(A[N])

=======
Suggestion 10

def insert_left(arr, i):
    arr.insert(0, i)
    return arr
