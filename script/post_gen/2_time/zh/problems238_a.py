Synthesizing 10/10 solutions

=======
Suggestion 1

def problem237_d():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(" ".join(map(str, A)))

=======
Suggestion 2

def solve():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(n):
        if s[i] == 'L':
            ans.insert(0, i+1)
        else:
            ans.append(i+1)
    print(*ans)

=======
Suggestion 3

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
Suggestion 4

def insert_left(target, index):
    target.insert(index-1, index)
    return target

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    for i in range(N):
        print(A[i], end=' ')
    print('')

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n-1):
        if s[i] == 'L':
            a.insert(0, i+2)
        else:
            a.append(i+2)
    print(" ".join(map(str, a)))

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0,i+1)
        else:
            a.append(i+1)
    for i in range(n+1):
        print(a[i],end=' ')

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N+1):
        if S[i-1] == 'L':
            A.insert(0,i)
        else:
            A.append(i)
    for i in A:
        print(i,end=' ')
    print()

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(n):
        if s[i] == "R":
            ans.append(i+1)
        else:
            ans.insert(0,i+1)
    print(" ".join(map(str,ans)))

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == 'L':
            L.append(i+1)
        else:
            R.append(i+1)
    L.reverse()
    print(' '.join(map(str, R+L)))
