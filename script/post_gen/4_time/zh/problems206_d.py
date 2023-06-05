Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    s = set()
    for i in range(n):
        if a[i] in s:
            ans += 1
            s.remove(a[i])
        else:
            s.add(a[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = {}
    for i in range(n):
        if a[i] not in b:
            b[a[i]] = 1
        else:
            b[a[i]] += 1
    ans = 0
    for i in b:
        if b[i] % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    import sys
    N = int(sys.stdin.readline().strip())
    A = [int(i) for i in sys.stdin.readline().strip().split()]
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    cnt = 0
    for i in d:
        if d[i] > 1:
            cnt += d[i] - 1
    print(cnt)

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n // 2):
        if a[i] != a[n - 1 - i]:
            ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    cnt = 0
    for i in range(n//2):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt*2 if n%2==0 else cnt*2+1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = 0
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            answer += 1
    print(answer)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = N
    count = 1
    for i in range(N-1):
        if A[i] == A[i+1]:
            count += 1
        else:
            ans -= count % 2
            count = 1
    ans -= count % 2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A.append(0)
    ans = 0
    i = 0
    while i < N:
        if A[i] == A[i+1]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
