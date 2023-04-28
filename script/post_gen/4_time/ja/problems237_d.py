Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    print(" ".join(map(str, A)))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N+1):
        if S[i-1] == 'L':
            A.insert(0,i)
        else:
            A.append(i)
    print(*A)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1,n):
        if s[i-1] == 'L':
            a.insert(0,i)
        else:
            a.append(i)
    print(*a)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.insert(i,a[i])
        else:
            a.insert(i+1,a[i]+1)
    print(" ".join(map(str,a)))
main()

=======
Suggestion 6

def solve():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N):
        if S[i-1] == "L":
            A.insert(0,i)
        else:
            A.append(i)
    print(*A)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(1, N):
        if S[i-1] == 'R':
            ans.append(i+1)
        else:
            ans.insert(0, i+1)
    print(*ans)

=======
Suggestion 8

def main():
    N = int(input())
    S = input()

    A = [0]
    for i in range(1, N):
        if S[i - 1] == "L" and S[i] == "R":
            A.append(i)
        elif S[i - 1] == "R" and S[i] == "L":
            A.append(i)
        elif S[i - 1] == "R" and S[i] == "R":
            A.append(i + 1)
        elif S[i - 1] == "L" and S[i] == "L":
            A.append(i)
    A.append(N)

    for i in range(N):
        print(A[i], end=" ")
    print(A[N])

=======
Suggestion 9

def solve():
    n = int(input())
    s = input()
    ans = []
    left = 0
    right = n
    for i in range(n):
        if s[i] == "L":
            ans.append(right)
            right -= 1
        else:
            ans.append(left)
            left += 1
    print(*ans[::-1])
solve()

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    
    ans = [0]
    for i in range(1, n):
        if s[i-1] == 'R' and s[i] == 'L':
            ans.append(i+1)
        elif s[i-1] == 'L' and s[i] == 'R':
            ans.append(i)
        else:
            ans.append(0)
    ans.append(0)
    
    print(' '.join(map(str, ans)))
