Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    sticks = list(map(int, input().split()))
    sticks.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if sticks[i] != sticks[j] and sticks[j] != sticks[k] and sticks[k] != sticks[i]:
                    if sticks[i] + sticks[j] > sticks[k]:
                        count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] < l[i] + l[j]:
                    res += 1
    print(res)

=======
Suggestion 5

def solve(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] != l[k] and l[i] + l[j] > l[k]:
                    ans += 1
    return ans

=======
Suggestion 6

def triangle_count(N, L):
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    count += 1
    return count

=======
Suggestion 7

def triangle(n, l):
    l.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                    if l[i] + l[j] > l[k]:
                        count += 1
    return count

n = int(input())
l = list(map(int, input().split()))
print(triangle(n, l))

=======
Suggestion 8

def isTriangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return 1
    else:
        return 0

=======
Suggestion 9

def triangle():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n - 2):
        a = l[i]
        for j in range(i + 1, n - 1):
            b = l[j]
            for k in range(j + 1, n):
                c = l[k]
                if a + b > c and a != b and b != c:
                    ans += 1
    print(ans)
triangle()

=======
Suggestion 10

def get_input():
    n = int(input())
    l = list(map(int, input().split()))
    return n, l
