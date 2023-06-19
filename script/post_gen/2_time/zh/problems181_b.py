Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B-A+1)*(A+B)//2
    print(sum)

=======
Suggestion 2

def sum_of_natural_numbers(n):
    return (1 + n) * n // 2

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) / 2
    print(int(sum))

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (b-a+1)*(a+b)/2
        sum = int(sum)
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (b - a + 1) * (a + b) // 2
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int, input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)

=======
Suggestion 7

def sum(n):
    return int(n*(n+1)/2)

n = int(input())
result = 0
for i in range(n):
    a,b = map(int,input().split())
    result += sum(b) - sum(a-1)
print(result)

=======
Suggestion 8

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a+b)*(b-a+1)/2
    print(int(sum))

=======
Suggestion 9

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        A, B = map(int, input().split())
        sum += (B - A + 1) * (A + B) / 2
    print(int(sum))

=======
Suggestion 10

def sum_of_integers_on_blackboard(n, a_list, b_list):
    sum = 0
    for i in range(n):
        sum += b_list[i] * (b_list[i] + 1) // 2
        sum -= a_list[i] * (a_list[i] - 1) // 2
    return sum
