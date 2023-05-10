Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] and p[i] < p[i+1]) or (p[i+1] < p[i] and p[i] < p[i-1]):
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p_list = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p_list[i-1] < p_list[i] < p_list[i+1] or p_list[i-1] > p_list[i] > p_list[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(n-2):
        if p[i] < p[i+1] and p[i+1] < p[i+2]:
            ans += 1
        elif p[i+2] < p[i+1] and p[i+1] < p[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i - 1] > p[i] > p[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i-1] > p[i] > p[i+1]):
            cnt += 1
    print(cnt)
