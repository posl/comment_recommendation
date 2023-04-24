Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            ans += 1
        if p[i] < p[i - 1] and p[i] > p[i + 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        if P[i-1] < P[i] < P[i+1] or P[i+1] < P[i] < P[i-1]:
            cnt += 1
    print(cnt)
