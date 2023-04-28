Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] < p[i + 1]) or (p[i - 1] > p[i] > p[i + 1]):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i-1] > p[i] > p[i+1]):
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i in range(1,n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(1,n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            count += 1
    print(count)
