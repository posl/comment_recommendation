Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int, input().split())
        sum += (b-a+1)*(a+b)/2
    print(int(sum))

=======
Suggestion 2

def problem181_b():
    n = int(input())
    sum = 0
    for i in range(n):
        a,b = map(int,input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)

=======
Suggestion 3

def sum_of_consecutive_numbers(a, b):
    return (a + b) * (b - a + 1) // 2

=======
Suggestion 4

def main():
    N = int(input())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += (a+b)*(b-a+1)//2
    print(sum)

=======
Suggestion 5

def f(a,b):
    return (a+b)*(b-a+1)//2

n = int(input())
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    ans += f(a,b)
print(ans)

=======
Suggestion 6

def problem181_b():
    N = int(input())
    sum = 0
    for i in range(N):
        A,B = map(int,input().split())
        sum += (B-A+1)*(A+B)/2
    print(int(sum))

=======
Suggestion 7

def solve(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i][1] - arr[i][0] + 1
    return sum

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    print(int(sum))

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    sum = 0
    for i in range(n):
        sum += (a[i] + b[i]) * (b[i] - a[i] + 1) / 2
    print(int(sum))

=======
Suggestion 10

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += (a+b)*(b-a+1)/2
    print(int(sum))
