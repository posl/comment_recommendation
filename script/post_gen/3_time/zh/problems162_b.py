Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def FizzBuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

N = int(input())
sum = 0
for i in range(1, N+1):
    sum += FizzBuzz(i)
print(sum)

=======
Suggestion 2

def fizzbuzz(n):
    result = 0
    for i in range(1,n+1):
        if i%3 == 0 and i%5 ==0:
            pass
        elif i%3 == 0:
            pass
        elif i%5 == 0:
            pass
        else:
            result += i
    return result

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
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
Suggestion 4

def is_divisible_by_3(n):
    return n % 3 == 0

=======
Suggestion 5

def FizzBuzz(n):
    sum = 0
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            sum += 0
        elif i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
        else:
            sum += i
    return sum

=======
Suggestion 6

def FizzBuzz(n):
    sum = 0
    for i in range(1,n+1):
        if i%15 == 0:
            sum += 0
        elif i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
        else:
            sum += i
    return sum

=======
Suggestion 7

def fizzbuzz(n):
    s = 0
    for i in range(1,n+1):
        if i % 15 == 0:
            s += 0
        elif i % 3 == 0:
            s += 0
        elif i % 5 == 0:
            s += 0
        else:
            s += i
    return s

n = int(input())
print(fizzbuzz(n))

=======
Suggestion 8

def FizzBuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i

=======
Suggestion 9

def main():
    n = int(input())
    print(sum([i for i in range(1, n+1) if i%3!=0 and i%5!=0 or i%15==0]))
