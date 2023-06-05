Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, p):
    count = 0
    for i in range(1, n - 1):
        if ((p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i + 1] < p[i] and p[i] < p[i - 1])):
            count += 1
    return count

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1,n-1):
        if p[i-1]<p[i] and p[i]<p[i+1]:
            count +=1
        if p[i-1]>p[i] and p[i]>p[i+1]:
            count +=1
    print(count)

=======
Suggestion 3

def get_second_smallest(arr):
    arr.sort()
    return arr[1]

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            count += 1
    print(count)

=======
Suggestion 6

def check(n, p):
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            count += 1
    return count

=======
Suggestion 7

def calc():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            count += 1
    print(count)

calc()

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)
