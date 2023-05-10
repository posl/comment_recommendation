Synthesizing 10/10 solutions

=======
Suggestion 1

def harvest():
    N = int(input())
    A = list(map(int, input().split()))
    harvest = 0
    for a in A:
        if a > 10:
            harvest += a - 10
    return harvest

print(harvest())

=======
Suggestion 2

def harvest(a):
    return a - 10 if a > 10 else 0

=======
Suggestion 3

def harvest_fruits(fruits):
    harvest = 0
    for fruit in fruits:
        if fruit > 10:
            harvest += fruit - 10
    return harvest

N = int(input())
A = list(map(int, input().split()))
print(harvest_fruits(A))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i > 10:
            ans += i - 10
    print(ans)

=======
Suggestion 5

def harvest(n, a):
    count = 0
    for i in range(n):
        if a[i] >= 10:
            count += a[i] - 10
    return count

=======
Suggestion 6

def harvest(n, a):
    total = 0
    for i in range(n):
        if a[i] > 10:
            total += a[i] - 10
    return total

=======
Suggestion 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] > 10:
            ans += a[i] - 10
    print(ans)

=======
Suggestion 8

def harvest(n, a_list):
    count = 0
    for i in range(n):
        if a_list[i] > 10:
            count += a_list[i] - 10
    return count

n = int(input())
a_list = list(map(int, input().split()))
print(harvest(n, a_list))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > 10:
            ans += A[i] - 10
    print(ans)

=======
Suggestion 10

def harvest(n, a):
    result = 0
    for i in range(n):
        if a[i] >= 10:
            result += a[i] - 10
    return result

n = int(input())
a = list(map(int, input().split()))
print(harvest(n, a))
