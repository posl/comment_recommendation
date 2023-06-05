Synthesizing 10/10 solutions

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
    print(sum(b) - sum(a) + n)

=======
Suggestion 2

def get_sum(a,b):
    return (a+b)*(b-a+1)//2

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) / 2
    print(int(sum))

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a + b) * (b - a + 1) // 2
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) / 2
    print(int(sum))

=======
Suggestion 6

def problem181_b():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (b-a+1)*(a+b)//2
    print(sum)

=======
Suggestion 8

def sum_range(start, end):
    return (start + end) * (end - start + 1) // 2

=======
Suggestion 9

def get_sum(start, end):
    if start == end:
        return start
    else:
        return (start + end) * (end - start + 1) // 2

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
