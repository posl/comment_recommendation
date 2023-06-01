Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_of_arithmetic_sequence(a1,an,n):
    return (a1+an)*n/2

n = int(input())
sum = 0
for i in range(n):
    ai, bi = map(int, input().split())
    sum += sum_of_arithmetic_sequence(ai,bi,bi-ai+1)
print(int(sum))

=======
Suggestion 2

def getSum(a, b):
    return (a + b) * (b - a + 1) // 2

n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += getSum(a, b)
print(sum)

=======
Suggestion 3

def sumOfIntervals(intervals):
    sum = 0
    for interval in intervals:
        sum += interval[1] - interval[0] + 1
    return sum

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) / 2
    print(int(sum))

=======
Suggestion 5

def sum_list(l):
    return sum(l)

=======
Suggestion 6

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) // 2
    print(sum)

=======
Suggestion 7

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) / 2
    print(int(sum))

=======
Suggestion 8

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a + b) * (b - a + 1) / 2
    print(int(sum))

=======
Suggestion 9

def sum_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += sum_natural_numbers(b) - sum_natural_numbers(a - 1)
print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    max_a = max(a)
    min_b = min(b)
    print(max(0, min_b - max_a + 1))
