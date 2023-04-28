Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
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
                if l[i] + l[j] > l[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
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
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] < l[j] + l[k] and l[j] < l[k] + l[i] and l[k] < l[i] + l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def check_triangle(a, b, c):
    if a < b + c and b < c + a and c < a + b:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] + L[j] > L[k]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    ans += 1
    print(ans)

=======
Suggestion 9

def solve(n, l):
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    return ans

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
