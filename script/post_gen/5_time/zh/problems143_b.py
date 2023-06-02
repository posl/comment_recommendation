Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def my_sum(a_list):
    if len(a_list) == 0:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + my_sum(a_list[1:])


n = int(input())
d = list(map(int, input().split()))
print(my_sum([d[i] * d[j] for i in range(len(d)) for j in range(i + 1, len(d))]))

=======
Suggestion 2

def solve():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i] * d[j]
    print(sum)

=======
Suggestion 3

def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += d[i]*d[j]
    print(sum)

=======
Suggestion 4

def sum_healths(n,ds):
    sum = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            sum += ds[i]*ds[j]
    return sum

=======
Suggestion 5

def solve():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum += d[i]*d[j]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += d[i] * d[j]
    print(ans)

=======
Suggestion 7

def sum_of_two_numbers(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            sum += numbers[i]*numbers[j]
    return sum
