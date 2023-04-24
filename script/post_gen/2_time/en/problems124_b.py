Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(N-1):
        if H[i] <= H[i+1]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(n-1):
        if h[i] <= h[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] >= max(H[:i+1]):
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 1
    max = h[0]
    for i in range(1, n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if all(h[i] >= h[j] for j in range(i)):
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    c = 0
    for i in range(1, n):
        if max(h[0:i]) <= h[i]:
            c += 1
    print(c+1)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(1, N):
        if all([H[j] <= H[i] for j in range(i)]):
            count += 1
    print(count + 1)

=======
Suggestion 8

def can_see_ocean(h):
    max_height = 0
    for i in h:
        if i >= max_height:
            max_height = i
        else:
            return False
    return True

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(len([i for i in range(1, N) if H[i-1] <= H[i]]))
