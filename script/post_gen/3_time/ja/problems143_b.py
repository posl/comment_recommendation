Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 4

def calc(n, d):
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    return sum

=======
Suggestion 5

def calc_sum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sum = sum + a[i] * a[j]
    return sum

=======
Suggestion 6

def calc_sum(a, b):
    return a * b

n = int(input())
d = list(map(int, input().split()))

sum = 0
for i in range(n):
    for j in range(i+1, n):
        sum += calc_sum(d[i], d[j])
print(sum)
