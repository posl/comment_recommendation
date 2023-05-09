Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] < L[j] + L[k] and L[j] < L[k] + L[i] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            a = L[i]
            b = L[j]
            k = j
            while k < N-1:
                if a+b <= L[k+1]:
                    break
                k += 1
            ans += k - j
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] + L[j] > L[k]:
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
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]+l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def count_triangles(L):
    L.sort()
    count = 0
    for i in range(len(L)-2):
        for j in range(i+1, len(L)-1):
            for k in range(j+1, len(L)):
                if L[i] + L[j] > L[k]:
                    count += 1
                else:
                    break
    return count

=======
Suggestion 7

def checkTriangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return 1
    else:
        return 0

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))

    l = sorted(l)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    count += 1

    print(count)

=======
Suggestion 9

def triangle(a,b,c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

=======
Suggestion 10

def main():
    # input
    N = int(input())
    L = list(map(int, input().split()))

    # compute

    # output
    print(ans)
