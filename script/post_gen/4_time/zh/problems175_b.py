Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_num_of_triangles_with_length(lengths):
    lengths.sort()
    num_of_triangles = 0
    for i in range(len(lengths)):
        for j in range(i+1, len(lengths)):
            for k in range(j+1, len(lengths)):
                if lengths[i] + lengths[j] > lengths[k]:
                    num_of_triangles += 1
    return num_of_triangles

=======
Suggestion 2

def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    return False

=======
Suggestion 3

def solve():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i]+L[j]:
                    ans += 1
    print(ans)

solve()

=======
Suggestion 4

def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                    if l[i] + l[j] > l[k]:
                        count += 1
    return count

=======
Suggestion 5

def getnum(n):
    n.sort()
    num=0
    for i in range(len(n)-2):
        for j in range(i+1,len(n)-1):
            for k in range(j+1,len(n)):
                if n[i]+n[j]>n[k]:
                    num+=1
    return num
n=int(input())
a=list(map(int,input().split()))
print(getnum(a))

=======
Suggestion 6

def triangle_number(n, a):
    a.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] + a[j] > a[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 7

def get_num_of_triangles(n, l):
    l.sort()
    num = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    num += 1
                else:
                    break
    return num

=======
Suggestion 8

def triangle_count(n, l):
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    count += 1
    return count

=======
Suggestion 9

def triangle_count(n, l):
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                    if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
                        count += 1
    return count

n = int(input())
l = list(map(int, input().split()))
print(triangle_count(n, l))
