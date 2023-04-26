Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    print(sum)

=======
Suggestion 2

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) / 2
    print(int(sum))

=======
Suggestion 3

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    ans = 0
    for i in range(n):
        ans += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    sum = 0
    for i in range(n):
        sum += (b[i] + a[i]) * (b[i] - a[i] + 1) // 2
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B-A+1)*(A+B)//2
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    print(sum(b) - sum(a) + n)

=======
Suggestion 7

def solve():
    N = int(input())
    sum = 0
    for i in range(N):
        A,B = map(int,input().split())
        sum += (B-A+1)*(A+B)/2
    print(int(sum))

=======
Suggestion 8

def main():
    N = int(input())
    sum = 0
    for i in range(0, N):
        a, b = map(int, input().split())
        sum += (b-a+1)*(a+b)//2
    print(sum)
