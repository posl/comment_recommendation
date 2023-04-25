Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
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
    ans = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] and p[i] < p[i + 1]) or (p[i + 1] < p[i] and p[i] < p[i - 1]):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            ans += 1
        elif p[i] < p[i - 1] and p[i] > p[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def second_smallest(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return b

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.append(0)
    count = 0
    for i in range(1, n + 1):
        if (p[i - 1] < p[i] < p[i + 1]) or (p[i - 1] > p[i] > p[i + 1]):
            count += 1
    print(count)

=======
Suggestion 8

def main():
    # read input
    n = int(input())
    p = list(map(int, input().split()))
    
    # count
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            count += 1
    print(count)
