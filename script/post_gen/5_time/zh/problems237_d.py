Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(i, i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 2

def solve():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0,i+1)
        else:
            a.append(i+1)
    print(*a)
solve()

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
    print(*A)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(1, n):
        if s[i] == 'L':
            ans.insert(0, i + 1)
        else:
            ans.append(i + 1)
    print(' '.join(map(str, ans)))

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n-1):
        if s[i] == 'L':
            a.insert(0,i+2)
        else:
            a.append(i+2)
    for i in a:
        print(i,end=' ')
    print('0')

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

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i + 1)
        else:
            a.append(i + 1)
    print(*a)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(' '.join(map(str, a)))

=======
Suggestion 9

def solve():
    n = int(input())
    s = input()
    l = []
    r = []
    for i in range(n):
        if s[i] == 'L':
            l.append(i+1)
        else:
            r.append(i+1)
    r.reverse()
    l.extend(r)
    print(' '.join(map(str,l)))
