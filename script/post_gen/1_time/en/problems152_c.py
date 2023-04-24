Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 1
    min_p = p[0]
    for i in range(1, n):
        if p[i] <= min_p:
            min_p = p[i]
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if P[i] == min(P[:i+1]):
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int,input().split()))
    ans = 0
    min = P[0]
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    minP = N+1
    for i in range(N):
        if P[i] <= minP:
            ans += 1
            minP = P[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            if P[i] <= min(P[:i+1]):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = N + 1
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    minP = 10**6
    for i in range(N):
        if P[i] < minP:
            count += 1
            minP = P[i]
    print(count)

=======
Suggestion 8

def solve(n, p):
    ans = 0
    m = p[0]
    for i in range(n):
        if m >= p[i]:
            ans += 1
            m = p[i]
    return ans

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    # print(n)
    # print(p)
    ans = 1
    min_p = p[0]
    for i in range(1, n):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # P[i] が P[j] 以下となる i, j を数える
    # 1 <= j <= i となる

    # P[i] が P[j] 以下となる i, j の組み合わせを数える
    # 1 <= j <= i となる

    # P[i] が P[j] 以下となる i, j の組み合わせのうち
    # P[i] が P[j] 以下となる i となる

    # P[i] が P[j] 以下となる i, j の組み合わせのうち
    # P[i] が P[j] 以下となる i となる
    # かつ P[i] が P[j] 以下となる j となる

    # P[i] が P[j] 以下となる i, j の組み合わせのうち
    # P[i] が P[j] 以下となる i となる
    # かつ P[i] が P[j] 以下となる j となる
    # かつ i == j となる

    # P[i] が P[j] 以下となる i, j の組み合わせのうち
    # P[i] が P[j] 以下となる i となる
    # かつ P[i] が P[j] 以下となる j となる
    # かつ i == j となる
    # かつ P[i] == P[j] となる

    # P[i] が P[j] 以下となる i, j の組み合わせのうち
    # P[i] が P[j] 以下となる i となる
    # かつ P[i] が P[j] 以下となる j となる
    # かつ i == j となる
