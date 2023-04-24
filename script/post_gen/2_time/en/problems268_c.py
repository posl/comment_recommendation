Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count//2)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n - 1:
                p[i + 1] = i + 1
            else:
                p[0] = 0
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i != N - 1:
                p[i], p[i + 1] = p[i + 1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    if count == N:
        print(N)
    else:
        print(N - count + 2 * (count % 2))

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i + 1 < N and p[i+1] == i + 1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i:
            if i == n-1:
                p[i], p[0] = p[0], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    num = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]:
            num += 1
    print(num)

=======
Suggestion 8

def main():
    n = int(input())
    p = map(int, input().split())
    p = [i-1 for i in p]
    result = 0
    for i in range(n):
        if p[i] == i:
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
            result += 1
    print(result)

=======
Suggestion 9

def main():
    N = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if (i + 1) == p[i]:
            if i == 0:
                if p[N - 1] == N - 1:
                    count += 1
            else:
                if p[i - 1] == i - 1:
                    count += 1

    print(count)

=======
Suggestion 10

def main():
    pass
