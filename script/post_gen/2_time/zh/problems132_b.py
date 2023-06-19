Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            count += 1
    print(count)

=======
Suggestion 2

def solve():
    n = int(input())
    p = [int(i) for i in input().split()]
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    return cnt

print(solve())

=======
Suggestion 3

def problem132_b():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] < p[i + 1]) or (p[i - 1] > p[i] > p[i + 1]):
            count += 1
    print(count)

=======
Suggestion 5

def get_second_min(p, i):
    if p[i-1] < p[i]:
        if p[i] < p[i+1]:
            return p[i]
        else:
            if p[i-1] < p[i+1]:
                return p[i+1]
            else:
                return p[i-1]
    else:
        if p[i] > p[i+1]:
            return p[i]
        else:
            if p[i-1] < p[i+1]:
                return p[i-1]
            else:
                return p[i+1]

n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    if get_second_min(p, i) == p[i]:
        count += 1
print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 8

def get_input():
    n = int(input())
    p = [int(i) for i in input().split()]
    return n, p
