Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    res = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            res += i
    print(res)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            sum += i
    print(sum)

=======
Suggestion 3

def f(n):
    if n % 15 == 0:
        return 0
    elif n % 3 == 0:
        return 1
    elif n % 5 == 0:
        return 2
    else:
        return 3

n = int(input())
sum = 0
for i in range(n):
    sum += i + 1 - f(i+1)
print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    print(sum)

=======
Suggestion 5

def fizz_buzz(n):
    s = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            s += 0
        elif i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
        else:
            s += i
    return s

=======
Suggestion 6

def f(n):
    if n % 15 == 0:
        return 0
    elif n % 3 == 0:
        return 1
    elif n % 5 == 0:
        return 2
    else:
        return 3

=======
Suggestion 7

def fizzbuzz(n):
    a = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            a += i
    return a

=======
Suggestion 8

def FizzBuzz(N):
    sum = 0
    for i in range(1, N+1):
        if i%3 == 0 and i%5 == 0:
            sum += i
        elif i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
    return sum

=======
Suggestion 9

def main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            continue
        elif i%3==0:
            continue
        elif i%5==0:
            continue
        else:
            sum += i
    print(sum)

=======
Suggestion 10

def FizzBuzz(n):
    sum = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            sum += i
    return sum
