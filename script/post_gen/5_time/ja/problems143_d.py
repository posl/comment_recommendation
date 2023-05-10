Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
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
Suggestion 2

def triangles(n, l):
    ans = 0
    l.sort()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
    return ans

n = int(input())
l = list(map(int, input().split()))
ans = triangles(n, l)
print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if(L[i] + L[j] > L[k]):
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

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

def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def check(a,b,c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=True)
#print(L)
count = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                count += 1
print(count)

=======
Suggestion 10

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)
