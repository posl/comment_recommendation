Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_odd_count(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            count += 1
    return count

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 2
        elif i < 10000:
            count += 2
        elif i < 100000:
            count += 3
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if len(str(i))%2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            count += 1
        elif i < 1000:
            count += 2
        elif i < 10000:
            count += 2
        elif i < 100000:
            count += 3
        else:
            count += 3
    print(count)

=======
Suggestion 5

def solve(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        else:
            if i % 2 == 1:
                count += 1
    return count

print(solve(100000))

=======
Suggestion 6

def main():
    #N = int(input())
    N = 100000
    count = 0
    for i in range(1, N+1):
        if i % 2 == 1:
            count += 1
        elif i % 10 == 1:
            count += 1
        elif i % 100 == 1:
            count += 1
        elif i % 1000 == 1:
            count += 1
        elif i % 10000 == 1:
            count += 1
        elif i % 100000 == 1:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 8

def odd_digits(n):
    count = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

=======
Suggestion 9

def get_odd_count(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            count += 1
    return count
