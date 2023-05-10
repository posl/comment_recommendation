Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    X = list(map(int, input().split()))
    min_sum = 10000000000000000
    for i in range(1, 101):
        sum = 0
        for j in range(N):
            sum += (X[j] - i) ** 2
        if sum < min_sum:
            min_sum = sum
    print(min_sum)

=======
Suggestion 2

def main():
    N = int(input())
    X = list(map(int, input().split()))

    result = float("inf")
    for i in range(1, 101):
        sum = 0
        for j in range(N):
            sum += (X[j] - i) ** 2
        result = min(result, sum)

    print(result)

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    min = 1000000
    for i in range(X[0], X[N-1]+1):
        sum = 0
        for j in range(N):
            sum += (X[j]-i)**2
        if sum < min:
            min = sum
    print(min)

=======
Suggestion 5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    min = 10000
    for i in range(1, 101):
        sum = 0
        for j in range(n):
            sum += (x[j] - i)**2
        if sum < min:
            min = sum
    print(min)

=======
Suggestion 6

def get_min_energy(n, x):
    min_energy = 100000000
    for i in range(1, 101):
        energy = 0
        for j in range(n):
            energy += (x[j] - i) ** 2
        if energy < min_energy:
            min_energy = energy
    return min_energy

=======
Suggestion 7

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(1, 101):
        sum = 0
        for j in range(n):
            sum += (x[j]-i)**2
        ans = min(ans, sum)
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**18
    for p in range(1, 101):
        tmp = 0
        for x in X:
            tmp += (x-p)**2
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 100000000
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    print(ans)
