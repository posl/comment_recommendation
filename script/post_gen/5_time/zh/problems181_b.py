Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    result = 0
    for i in range(n):
        a,b = map(int,input().split())
        result += (b-a+1)*(a+b)/2
    print(int(result))

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a + b) * (b - a + 1) // 2
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (b-a+1)*(a+b)/2
    print(int(sum))

=======
Suggestion 4

def solve(n, ranges):
    # write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    total = 0
    for i in range(n):
        total += (ranges[i][1] - ranges[i][0] + 1) * (ranges[i][1] + ranges[i][0]) / 2
    return int(total)

n = int(input())
ranges = []
for _ in range(n):
    ranges.append(list(map(int, input().split())))
print(solve(n, ranges))

=======
Suggestion 5

def func(n, a, b):
    res = 0
    for i in range(n):
        res += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    return res

=======
Suggestion 6

def getSum(start, end):
    return (start + end) * (end - start + 1) // 2

n = int(input())
sum = 0
for i in range(n):
    start, end = map(int, input().split())
    sum += getSum(start, end)
print(sum)

=======
Suggestion 7

def solve(n, a, b):
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (b[i] + a[i]) / 2
    return sum

=======
Suggestion 8

def solve():
    N = int(input())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) // 2
    print(sum)
solve()

=======
Suggestion 9

def solve(n, a, b):
    total = 0
    for i in range(n):
        total += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    return total

=======
Suggestion 10

def sum_of_n(n):
    return (n * (n + 1)) // 2

n = int(input())
sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += sum_of_n(b) - sum_of_n(a - 1)
print(sum)
