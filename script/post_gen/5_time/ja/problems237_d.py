Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N):
        if S[i-1] == 'L' and S[i] == 'R':
            A.append(i)
        elif S[i-1] == 'R' and S[i] == 'L':
            A.append(i)
    A.append(N)
    for i in range(N):
        print(A[i+1]-A[i],end=' ')
    print()

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    ans = [0]*(n+1)
    l = 0
    r = n
    for i in range(n):
        if s[i] == "L":
            ans[r] = i+1
            r -= 1
        else:
            ans[l] = i+1
            l += 1
    print(*ans)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N+1):
        if S[i-1] == 'L':
            A.insert(0,i)
        else:
            A.append(i)
    print(*A)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1,n+1):
        if s[i-1] == "L":
            a.insert(0,i)
        else:
            a.append(i)
    print(*a)

=======
Suggestion 6

def solve():
    n = int(input())
    s = input()
    ans = [0] * (n + 1)
    cnt = 0
    for i in range(n):
        if s[i] == 'L':
            ans[i + 1] = i + 1
            ans[i] = i + 2
            cnt = i + 2
        else:
            ans[i + 1] = cnt
            cnt += 1
    print(*ans)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = []
    ans.append(0)
    for i in range(n-1):
        if s[i] == "L":
            ans.insert(0,i+1)
        else:
            ans.append(i+1)
    print(*ans)
main()

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    ans = []
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l = l + 1
            ans.append(l)
        else:
            r = r + 1
            ans.insert(0, r)
    print(' '.join(map(str, ans)))
