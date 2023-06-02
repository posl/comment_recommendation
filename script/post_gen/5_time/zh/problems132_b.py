Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def problem132_b():
    n = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            count += 1
    print(count)

=======
Suggestion 3

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

solve()

=======
Suggestion 4

def get_second_smallest_number(p):
    if p[0] < p[1]:
        if p[1] < p[2]:
            return p[1]
        else:
            return p[2]
    else:
        if p[0] < p[2]:
            return p[0]
        else:
            return p[2]

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] < p[i + 1]) or (p[i + 1] < p[i] < p[i - 1]):
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 7

def find_second_min(array):
    if array[0] < array[1]:
        min = array[0]
        second_min = array[1]
    else:
        min = array[1]
        second_min = array[0]
    for i in range(2, len(array)):
        if array[i] < min:
            second_min = min
            min = array[i]
        elif array[i] < second_min:
            second_min = array[i]
    return second_min

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i - 1] > p[i] and p[i] > p[i + 1]):
            count += 1
    print(count)
