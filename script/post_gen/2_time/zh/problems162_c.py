Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print(sum([i for i in range(1, n + 1) if i % 3 != 0 and i % 5 != 0 or i % 15 == 0]))

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1,n+1):
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
Suggestion 3

def fizzbuzz(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    return sum

=======
Suggestion 4

def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        result += i
    print(result)

=======
Suggestion 5

def FizzBuzz(n):
    s = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            s += i
        elif i % 3 == 0:
            s += i
        elif i % 5 == 0:
            s += i
    return s

=======
Suggestion 6

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
Suggestion 7

def FizzBuzz(n):
    sum=0
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            sum=sum
        elif i%3==0:
            sum=sum
        elif i%5==0:
            sum=sum
        else:
            sum=sum+i
    return sum

=======
Suggestion 8

def FizzBuzz(n):
    sum = 0
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    return sum

n = int(input())
print(FizzBuzz(n))

=======
Suggestion 9

def f(n):
    if n%15 == 0:
        return 0
    elif n%5 == 0:
        return 1
    elif n%3 == 0:
        return 2
    else:
        return 3

N = int(input())
ans = 0
for i in range(1,N+1):
    ans += f(i)*i
print(ans)

=======
Suggestion 10

def func(n):
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
