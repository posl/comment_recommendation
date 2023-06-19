Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        for i in range(N):
            if A[i] <= x <= B[i]:
                continue
            else:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(max(0, min(B) - max(A) + 1))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_a = max(a)
    min_b = min(b)
    print(min_b - max_a + 1 if min_b - max_a >= 0 else 0)

main()

=======
Suggestion 4

def get_int():
    return int(input())

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for x in range(1, 1001):
        if all(a[i] <= x <= b[i] for i in range(n)):
            count += 1
    print(count)

=======
Suggestion 6

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for x in range(1, 1001):
        ok = True
        for i in range(n):
            if x < a[i] or x > b[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max(min(b) - max(a) + 1, 0))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        count += b[i] - a[i] + 1
    print(count)

=======
Suggestion 9

def count(x, a, b):
    count = 0
    for i in range(len(a)):
        if a[i] <= x <= b[i]:
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for x in range(1, 1001):
    if count(x, a, b) == n:
        ans += 1

print(ans)
