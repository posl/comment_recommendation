Synthesizing 10/10 solutions

=======
Suggestion 1

def FizzBuzz(n):
    sum = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        sum += i
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        else:
            sum += i
    print(sum)

=======
Suggestion 5

def solve(N):
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
    return sum

=======
Suggestion 6

def FizzBuzz(N):
    sum = 0
    for i in range(1, N+1):
        if i%3 == 0 and i%5 == 0:
            pass
        elif i%3 == 0:
            pass
        elif i%5 == 0:
            pass
        else:
            sum += i
    return sum

=======
Suggestion 7

def getFizzBuzzSum(n):
    sum = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    return sum

=======
Suggestion 8

def f(n):
    if n % 15 == 0:
        return 0
    elif n % 5 == 0:
        return n
    elif n % 3 == 0:
        return n
    else:
        return n

=======
Suggestion 9

def FizzBuzz(n):
    sum = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        else:
            sum += i
    return sum

=======
Suggestion 10

def FizzBuzz(N):
    sum=0
    for i in range(1,N+1):
        if i%3==0 and i%5==0:
            sum=sum
        elif i%3==0:
            sum=sum
        elif i%5==0:
            sum=sum
        else:
            sum=sum+i
    return sum

N=int(input())
print(FizzBuzz(N))
