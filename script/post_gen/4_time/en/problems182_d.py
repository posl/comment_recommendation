Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(n):
        x += a[i]
        ans = max(ans, x)
    print(ans)
main()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    x = 0
    for i in range(n):
        x += a[i]
        ans = max(ans, x)
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    x = 0
    for a in A:
        x += a
        ans = max(ans, x)
    return ans

print(solve())

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    now = 0
    for i in range(N):
        now += A[i]
        ans = max(ans, now)
    print(ans)
solve()

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    s.sort()
    ans = 0
    for i in range(N):
        ans = max(ans, s[i + 1] - s[i])
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > max:
            max = sum
    print(max)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if abs(sum) > max:
            max = abs(sum)
    print(max)
main()

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
        A[i] = ans
    print(max(A))
solve()

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    max_pos = 0
    for i in range(n):
        total += a[i]
        if total > max_pos:
            max_pos = total
    return max_pos

print(solve())

=======
Suggestion 10

def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

n=int(input())
a=list(map(int,input().split()))

print(max([sum(a[:i+1]) for i in range(n)]))
