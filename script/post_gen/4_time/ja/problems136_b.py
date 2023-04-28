Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 6

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    result = 0
    for i in range(1,n+1):
        if len(str(i)) % 2 == 1:
            result += 1
    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if len(str(i))%2 != 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def count_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count
