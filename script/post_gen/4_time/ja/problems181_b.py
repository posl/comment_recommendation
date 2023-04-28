Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += (a + b) * (b - a + 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for _ in range(N):
        A, B = map(int, input().split())
        ans += (A + B) * (B - A + 1) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        A, B = map(int, input().split())
        ans += (B - A + 1) * (A + B) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (A + B) * (B - A + 1) // 2
    print(sum)

=======
Suggestion 7

def solve():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (a+b)*(b-a+1)//2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        A, B = map(int, input().split())
        ans += (B-A+1)*(A+B)/2
    print(int(ans))

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    print(int(sum))

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(sum(b) - sum(a) + n)
