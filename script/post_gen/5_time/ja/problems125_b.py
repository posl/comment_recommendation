Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    s = 0
    for i in range(n):
        if v[i] > c[i]:
            s += v[i] - c[i]
    print(s)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        tmp = v[i] - c[i]
        if tmp > 0:
            ans += tmp
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            result += v[i] - c[i]
    print(result)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x = 0
    y = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i]
            y += c[i]
    print(x-y)

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i]-c[i]
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]

    print(ans)

main()
