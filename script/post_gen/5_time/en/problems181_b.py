Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a + b) * (b - a + 1) // 2
    print(sum)

=======
Suggestion 2

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) // 2
    print(sum)

=======
Suggestion 3

def solve():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) // 2
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int, input().split())
        sum += (a+b)*(b-a+1)/2
    print(int(sum))

=======
Suggestion 5

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
        sum += (b[i] + a[i]) * (b[i] - a[i] + 1) / 2
    print(int(sum))

=======
Suggestion 6

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
Suggestion 7

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int, input().split())
        sum += (b-a+1)*(a+b)/2
    print(int(sum))

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(sum(B)-sum(A)+N)

=======
Suggestion 9

def main():
    n = int(input())
    total = 0
    for i in range(n):
        a,b = map(int,input().split())
        total += (b-a+1)*(a+b)/2
    print(int(total))

main()

=======
Suggestion 10

def sum_of_integers(n, a, b):
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    return sum

n = int(input())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

print(int(sum_of_integers(n, a, b)))
