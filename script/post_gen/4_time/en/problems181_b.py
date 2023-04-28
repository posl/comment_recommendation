Synthesizing 10/10 solutions (Duplicates hidden)

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
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a + b) * (b - a + 1) / 2
    print(int(sum))

=======
Suggestion 3

def main():
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
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(sum(b) - sum(a) + n)

=======
Suggestion 5

def sum(n):
    return n * (n + 1) // 2

n = int(input())
sum = 0
for i in range(n):
    a,b = map(int, input().split())
    sum += sum(b) - sum(a - 1)
print(sum)

=======
Suggestion 6

def sum_range(a, b):
    return (a + b) * (b - a + 1) // 2

=======
Suggestion 7

def sum_of_natural_nums(n):
    return n*(n+1)/2

n = int(raw_input())
sum = 0
for i in range(n):
    a, b = map(int, raw_input().split())
    sum += sum_of_natural_nums(b) - sum_of_natural_nums(a-1)
print sum
