Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
    result = 0
    for d in D:
        if d <= X:
            result += 1
    print(result)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    count = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    count = 1
    for i in range(N):
        D = D + L[i]
        if D <= X:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N+1)
    D[0] = 0
    for i in range(1, N+1):
        D[i] = D[i-1] + L[i-1]
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    for i in range(n):
        d += l[i]
        if d > x:
            break
    print(i+1)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in D:
        if i <= X:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    count = 1
    sum = 0
    for i in range(N):
        sum = sum + L[i]
        if sum <= X:
            count = count + 1
    print(count)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))

    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])

    cnt = 0
    for i in range(n + 1):
        if d[i] <= x:
            cnt += 1

    print(cnt)
