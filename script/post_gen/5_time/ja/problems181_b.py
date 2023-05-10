Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    sum = 0
    for i in range(N):
        sum += (B[i] - A[i] + 1)*(A[i] + B[i])/2
    print(int(sum))

main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        ans += (a + b) * (b - a + 1) // 2
    print(ans)

=======
Suggestion 3

def calc():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)
calc()

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(sum(b) - sum(a) + n)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(sum(B) - sum(A) + N)

=======
Suggestion 6

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
        sum += (a[i] + b[i]) * (b[i] - a[i] + 1) / 2

    print(int(sum))

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    print(sum(b) - sum(a) + n)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)

=======
Suggestion 9

def calc_sum(a, b):
    return (a + b) * (b - a + 1) // 2

n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += calc_sum(a, b)
print(ans)
