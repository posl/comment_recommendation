Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if (p[i - 1] < p[i] < p[i + 1]) or (p[i + 1] < p[i] < p[i - 1]):
            ans += 1
    print(ans)

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] and p[i] < p[i+1]:
            count += 1
        elif p[i+1] < p[i] and p[i] < p[i-1]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int,input().split()))

    cnt = 0
    for i in range(1,N-1):
        if p[i-1] < p[i] < p[i+1]:
            cnt += 1
        elif p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    #入力
    n = int(input())
    p = list(map(int, input().split()))
    #処理
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            count += 1
    #出力
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    #print(n, p)

    count = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1]:
            count += 1
        elif p[i + 1] < p[i] < p[i - 1]:
            count += 1
    print(count)
