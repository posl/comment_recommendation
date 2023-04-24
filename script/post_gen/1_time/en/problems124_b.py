Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))

    max = 0
    count = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
            count += 1

    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = H[0]
    cnt = 1
    for i in range(1, N):
        if maxH <= H[i]:
            cnt += 1
            maxH = H[i]
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    max = 0

    for i in range(N):
        if H[i] >= max:
            cnt += 1
            max = H[i]

    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif h[i] >= max(h[:i]):
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max = 0
    c = 0
    for i in range(n):
        if h[i] >= max:
            max = h[i]
            c += 1
    print(c)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))

    cnt = 0
    max_h = 0
    for i in h:
        if i >= max_h:
            cnt += 1
            max_h = i

    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    highest = h[0]
    for i in range(1, n):
        if h[i] >= highest:
            count += 1
        highest = max(highest, h[i])
    print(count + 1)

=======
Suggestion 10

def find_ocean_inns():
    n = int(input())
    H = list(map(int, input().split()))
    ocean_inns = 1
    for i in range(1, n):
        if max(H[:i]) <= H[i]:
            ocean_inns += 1
    return ocean_inns

print(find_ocean_inns())
