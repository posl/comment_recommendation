Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num_triangle(N, L):
    L.sort()
    num_triangle = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        num_triangle += 1
    return num_triangle

=======
Suggestion 2

def problem175_b():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                    if l[i] + l[j] > l[k]:
                        count += 1
    print(count)

problem175_b()

=======
Suggestion 3

def triangle():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def triangle(N, L):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k]:
                    if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                        count += 1
    return count

=======
Suggestion 5

def main():
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]!=l[j] and l[j]!=l[k] and l[i]+l[j]>l[k]:
                    count+=1
    print(count)

=======
Suggestion 6

def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if isTriangle(L[i],L[j],L[k]):
                ans += 1

print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def triangle(L):
    L.sort()
    count = 0
    for i in range(len(L)-2):
        for j in range(i+1, len(L)-1):
            for k in range(j+1, len(L)):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k]:
                    if L[i] + L[j] > L[k]:
                        count += 1
    return count

=======
Suggestion 9

def count_triangles(n, l):
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    count += 1
    return count

=======
Suggestion 10

def triangles():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i]+L[j] > L[k] and L[i]!=L[j] and L[j]!=L[k]:
                    cnt += 1
    print(cnt)
