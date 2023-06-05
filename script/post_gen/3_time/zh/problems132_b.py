Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            count += 1
    print(count)

=======
Suggestion 2

def solve():
    n = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(1,n-1):
        if (p[i-1]<p[i]<p[i+1]) or (p[i-1]>p[i]>p[i+1]):
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def get_number_of_elements(n, p):
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    return count

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] and p[i] < p[i + 1]:
            count += 1
        elif p[i + 1] < p[i] and p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] and p[i] < p[i+1]:
            cnt += 1
        elif p[i+1] < p[i] and p[i] < p[i-1]:
            cnt += 1
    print(cnt)
