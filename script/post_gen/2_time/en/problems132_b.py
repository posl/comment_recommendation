Synthesizing 10/10 solutions

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
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i] < max(p[i - 1], p[i + 1]) and p[i] > min(p[i - 1], p[i + 1]):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if p[i] > min(p[i - 1], p[i + 1]) and p[i] < max(p[i - 1], p[i + 1]):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        if sorted(p[i-1:i+2])[1] == p[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    cnt = 0
    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] < p[i + 1]:
            cnt += 1
        elif p[i] < p[i - 1] and p[i] > p[i + 1]:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    p = input().split()
    for i in range(n):
        p[i] = int(p[i])
    count = 0
    for i in range(1, n-1):
        if p[i] > p[i-1] and p[i] < p[i+1]:
            count += 1
        elif p[i] < p[i-1] and p[i] > p[i+1]:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = [int(p) for p in input().split()]
    ans = 0
    for i in range(1, N - 1):
        if P[i - 1] < P[i] < P[i + 1] or P[i + 1] < P[i] < P[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))

    # p[i]がp[i-1], p[i], p[i+1]の中で2番目に小さい値であるかどうかを判定する
    # 2番目に小さい値を求めるには、3つの値のうち最大値と最小値を求めればよい

    ans = 0
    for i in range(1, n - 1):
        if p[i] > max(p[i - 1], p[i + 1]) or p[i] < min(p[i - 1], p[i + 1]):
            continue
        ans += 1

    print(ans)
