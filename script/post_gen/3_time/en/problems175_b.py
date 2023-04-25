Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i]+l[j]>l[k] and l[i]!=l[j] and l[j]!=l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] == l[j] or l[j] == l[k]:
                    continue
                if l[i] + l[j] > l[k]:
                    ans += 1
                else:
                    break
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
                if l[i]!=l[j] and l[j]!=l[k] and l[i]+l[j]>l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def triangle(n, l):
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k]:
                    count += 1
    return count

n = int(input())
l = list(map(int, input().split()))
print(triangle(n, l))

=======
Suggestion 7

def triangle(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k] and l[i]+l[j] > l[k]:
                    count += 1
    return count

=======
Suggestion 8

def triangle():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    count = 0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i]+l[j]>l[k]:
                    count += 1
    print(count)
triangle()

=======
Suggestion 9

def count_triangles(arr):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] > arr[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 10

def triangle_count():
    # input
    n = int(input())
    l = list(map(int, input().split()))

    # sort
    l.sort()

    # count
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                    continue
                if l[i] + l[j] > l[k]:
                    ans += 1

    # output
    print(ans)
