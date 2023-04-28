Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10 ** 10
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10 ** 9
    for i in range(x[0], x[-1] + 1):
        s = 0
        for j in x:
            s += (j - i) ** 2
        if s < ans:
            ans = s
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))

    ans = 0
    for i in range(101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        if i == 0:
            ans = tmp
        else:
            ans = min(ans, tmp)

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    X = list(map(int, input().split()))
    min_cost = 1000000000
    for i in range(1, 101):
        cost = 0
        for j in range(N):
            cost += (X[j] - i) ** 2
        if min_cost > cost:
            min_cost = cost
    print(min_cost)

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 10**9
    for i in range(x[0], x[-1]+1):
        total = 0
        for j in range(n):
            total += (x[j] - i) ** 2
        ans = min(ans, total)
    print(ans)

=======
Suggestion 7

def calc_sum(x, p):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - p) ** 2
    return sum

=======
Suggestion 8

def main():
    N = int(input())
    X = list(map(int, input().split()))
    min = 1000000000
    for i in range(1,100):
        sum = 0
        for j in range(N):
            sum += (X[j] - i)**2
        if sum < min:
            min = sum
    print(min)

=======
Suggestion 9

def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    ans = 1000000000000
    for p in range(1,101):
        tmp = 0
        for i in range(n):
            tmp += (x[i] - p) ** 2
        ans = min(ans,tmp)
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    min = 100000000000000000
    for i in range(x[0],x[n-1]+1):
        sum = 0
        for j in range(0,n):
            sum = sum + (x[j]-i)**2
        if sum < min:
            min = sum
    print(min)
