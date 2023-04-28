Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i]+l[j] > l[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i]+l[j]>l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 6

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def check(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    return False

=======
Suggestion 8

def solve():
    N = int(input())
    L = list(map(int,input().split()))
    cnt = 0
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                if L[a] < L[b] + L[c] and L[b] < L[c] + L[a] and L[c] < L[a] + L[b]:
                    cnt += 1
    print(cnt)

=======
Suggestion 9

def triangles():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    count += 1
                else:
                    break
    print(count)
triangles()

=======
Suggestion 10

def triangle_count(n, l):
    l.sort()
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    cnt += 1
    return cnt

n = int(input())
l = list(map(int, input().split()))
print(triangle_count(n, l))
