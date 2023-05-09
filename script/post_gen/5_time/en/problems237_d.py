Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(" ".join(map(str, A)))

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(' '.join([str(_) for _ in a]))

=======
Suggestion 4

def main():
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
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    print(*A)

=======
Suggestion 7

def solve():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0,i+1)
        else:
            A.append(i+1)
    print(' '.join(map(str,A)))

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1,n):
        if s[i-1] == "R":
            a.append(i)
        else:
            a.insert(0,i)
    print(*a)

=======
Suggestion 9

def get_input():
    n = int(input())
    s = input()
    return n, s
