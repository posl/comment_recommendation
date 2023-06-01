Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    a = [0] + a
    ans = 0
    for i in xrange(1, n + 1):
        if a[a[i]] == i:
            ans += 1
    print ans / 2

=======
Suggestion 2

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i
    ans = 0
    min_pos = n
    max_pos = -1
    for i in range(n):
        min_pos = min(min_pos, b[i])
        max_pos = max(max_pos, b[i])
        if max_pos - min_pos == i:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i + 1 == a[i]:
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def problem262_c():
    n = int(input())
    data = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if min(data[i], data[j]) == i+1 and max(data[i], data[j]) == j+1:
                count += 1
    print(count)

=======
Suggestion 5

def problems262_c():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] <= i + 1:
            continue
        for j in range(i + 1, n):
            if a[i] == j + 1 and a[j] == i + 1:
                count += 1
    print(count)

=======
Suggestion 7

def count_min_max(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if min(a[i],a[j]) == i+1 and max(a[i],a[j]) == j+1:
                count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in range(n):
        b[a[i]] = i+1
    ans = 0
    for i in range(1, n+1):
        if b[i] == i:
            ans += 1
        else:
            if b[i] > b[i+1]:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    min_value = [0] * (n + 1)
    max_value = [0] * (n + 1)
    for i in range(n):
        min_value[a[i]] = i + 1
        max_value[a[i]] = i + 1
    for i in range(1, n + 1):
        min_value[i] = max(min_value[i], min_value[i - 1])
    for i in range(n - 1, 0, -1):
        max_value[i] = min(max_value[i], max_value[i + 1])
    ans = 0
    for i in range(1, n + 1):
        ans += max_value[i] - min_value[i]
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > i + 1:
            continue
        for j in range(i + 1, N):
            if A[i] == j + 1 and A[j] == i + 1:
                ans += 1
    print(ans)
