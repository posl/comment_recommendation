Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_p = n + 1
    for i in range(n):
        if p[i] <= min_p:
            count += 1
            min_p = p[i]
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    min = n
    for i in range(n):
        if p[i] <= min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    min = n+1
    for i in range(n):
        if p[i] <= min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = N
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    min = n + 1
    for i in range(n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = n + 1
    for i in range(n):
        if min > p[i]:
            ans += 1
            min = p[i]
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    min = N+1
    count = 0
    for i in range(N):
        if min > P[i]:
            min = P[i]
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    min = n
    for i in p:
        if i <= min:
            ans += 1
            min = i
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    result = 0
    min = n
    for i in range(n):
        if min > p[i]:
            min = p[i]
            result += 1
    print(result)

=======
Suggestion 10

def count_bigger_than_all_previous_numbers(numbers):
    count = 0
    min = numbers[0]
    for number in numbers:
        if number <= min:
            min = number
            count += 1
    return count
