Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 2

def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(sum([d[i]*d[j] for i in range(n) for j in range(i+1, n)]))

=======
Suggestion 5

def takoyaki_festival():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    d = list(map(int, input().split()))

    sum = 0

    for i in range(n):
        for j in range(i+1, n):
            sum = sum + (d[i] * d[j])

    print(sum)

=======
Suggestion 7

def takoyaki_festival(N, d):
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            result += d[i] * d[j]
    return result

=======
Suggestion 8

def sum_takoyaki(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum = sum + d[i]*d[j]
    return sum

N = int(input())
d = list(map(int, input().split()))
print(sum_takoyaki(N, d))

=======
Suggestion 9

def sum_of_all_pairs(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum += arr[i] * arr[j]
    return sum
