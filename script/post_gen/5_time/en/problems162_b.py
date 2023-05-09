Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += fizzbuzz(i)
print(ans)

=======
Suggestion 2

def fizzbuzz(n):
    sum = 0
    for i in range(1, n+1):
        if i % 15 == 0:
            continue
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

=======
Suggestion 3

def main():
    N = int(input())
    sum = 0
    for i in range(1, N + 1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        sum += i
    print(sum)

main()

=======
Suggestion 4

def fizzbuzz(n):
    sum = 0
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            pass
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            sum += i
    return sum

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

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        if (i+1)%3 != 0 and (i+1)%5 != 0:
            sum += i+1
    print(sum)

=======
Suggestion 7

def main():
    n = int(input())
    print(sum([i for i in range(1,n+1) if i%3 != 0 and i%5 != 0]))

=======
Suggestion 8

def sum_of_fizzbuzz(n):
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
    return sum

=======
Suggestion 9

def fizzbuzz(n):
    return n*(n+1)//2 - (n//3)*(n//3 + 1)//2*3 - (n//5)*(n//5 + 1)//2*5 + (n//15)*(n//15 + 1)//2*15

n = int(input())
print(fizzbuzz(n))
