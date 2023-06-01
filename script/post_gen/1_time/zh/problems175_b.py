Synthesizing 10/10 solutions

=======
Suggestion 1

def triangle(L):
    L.sort()
    cnt = 0
    for i in range(len(L)-2):
        for j in range(i+1,len(L)-1):
            for k in range(j+1,len(L)):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    cnt += 1
    return cnt

N = int(input())
L = list(map(int,input().split()))
print(triangle(L))

=======
Suggestion 2

def triangle(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k]:
                        ans += 1
    return ans

=======
Suggestion 3

def triangle():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def triangles(l):
    l.sort()
    n = len(l)
    cnt = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    cnt += 1
    return cnt

=======
Suggestion 5

def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    count += 1
                elif l[k] >= l[i] + l[j]:
                    break
    return count

=======
Suggestion 6

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i]+L[j] > L[k]:
                    cnt += 1
    print(cnt)
main()

=======
Suggestion 8

def isTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if isTriangle(l[i], l[j], l[k]):
                ans += 1
print(ans)

=======
Suggestion 9

def triangle(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]+l[j] > l[k] and l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    ans += 1
    return ans

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
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i]+L[j] > L[k]:
                    ans += 1
    print(ans)
solve()
