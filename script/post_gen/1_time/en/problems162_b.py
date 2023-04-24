Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        ans += i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            sum += i
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            ans += i
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            sum += i
    print(sum)

=======
Suggestion 6

def fizzbuzz(n):
    a, b, c = 0, 0, 0
    for i in range(1, n+1):
        if i % 3 == 0:
            a += i
        if i % 5 == 0:
            b += i
        if i % 15 == 0:
            c += i
    return a + b - c

=======
Suggestion 7

def fizzbuzz(n):
    return [i if i%3 and i%5 else 'FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' for i in range(1,n+1)]

=======
Suggestion 8

def main():
    N = int(input())
    print(sum([i for i in range(1, N+1) if i%3 != 0 and i%5 != 0]))

=======
Suggestion 9

def main():
    n = int(input())
    if n <= 0:
        return 0
    else:
        return fizzbuzz(n)
