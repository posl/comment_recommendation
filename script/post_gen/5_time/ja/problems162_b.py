Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    N = int(input())

    # compute
    ans = 0
    for i in range(1, N+1):
        if i%3==0 or i%5==0:
            continue
        else:
            ans += i

    # output
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return n

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += fizzbuzz(i)
print(sum)

=======
Suggestion 4

def fizzbuzz(n):
    if n%15==0:
        return "FizzBuzz"
    elif n%5==0:
        return "Buzz"
    elif n%3==0:
        return "Fizz"
    else:
        return str(n)

=======
Suggestion 5

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if i%3 == 0 or i%5 == 0:
            continue
        else:
            ans += i
    print(ans)

=======
Suggestion 6

def fizzbuzz(n):
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        ans += i
    return ans

=======
Suggestion 7

def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += fizzbuzz(i)
print(ans)

=======
Suggestion 8

def fizzbuzz(n):
    if n%15 == 0:
        return "FizzBuzz"
    if n%3 == 0:
        return "Fizz"
    if n%5 == 0:
        return "Buzz"
    return str(n)

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i if fizzbuzz(i) == str(i) else 0
print(ans)

=======
Suggestion 9

def FizzBuzz(x):
    if x%3==0 and x%5==0:
        return "FizzBuzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return "Buzz"
    else:
        return str(x)

n=int(input())
s=0
for i in range(1,n+1):
    s+=int(FizzBuzz(i))
print(s)
