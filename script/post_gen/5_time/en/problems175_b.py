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
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 3

def is_triangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

n = int(input())
l = list(map(int, input().split()))

l.sort()

count = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if is_triangle(l[i], l[j], l[k]):
                count += 1

print(count)

=======
Suggestion 4

def triangle(N, L):
    L.sort()
    count = 0
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    count += 1
    return count

=======
Suggestion 5

def triangles(N, L):
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    return ans

=======
Suggestion 6

def solve():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    count += 1
    return count

=======
Suggestion 7

def triangle_count(n, lines):
    lines.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if lines[i] + lines[j] > lines[k]:
                    count += 1
    return count

=======
Suggestion 8

def check_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

=======
Suggestion 9

def findTriangleCount(arr):
    count = 0
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] != arr[j] and arr[j] != arr[k] and arr[i] != arr[k]:
                    if arr[i] + arr[j] > arr[k] and arr[j] + arr[k] > arr[i] and arr[i] + arr[k] > arr[j]:
                        count += 1
    return count

=======
Suggestion 10

def get_input():
    n = int(input())
    l = list(map(int, input().split()))
    return n, l
