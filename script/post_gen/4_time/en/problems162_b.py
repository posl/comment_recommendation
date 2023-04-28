Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 != 0 and i % 5 != 0:
            sum += i
    print(sum)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        sum += i
    print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            ans += i
    print(ans)
    return

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            pass
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            sum += i
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            ans += i
    print(ans)

=======
Suggestion 6

def fizzbuzz(n):
    total = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            total += i
    return total

=======
Suggestion 7

def solve():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        sum += i
    print(sum)

=======
Suggestion 8

def solve(n):
    sum = 0
    for i in range(1, n+1):
        if (i % 3 != 0 and i % 5 != 0):
            sum += i
    return sum

=======
Suggestion 9

def main():
    n = int(input())
    print(sum([i for i in range(1,n+1) if i%3 != 0 and i%5 != 0]))
