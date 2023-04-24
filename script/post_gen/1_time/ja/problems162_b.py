Synthesizing 10/10 solutions

=======
Suggestion 1

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

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
    ans = 0
    for i in range(1, N+1):
        if i % 15 == 0:
            ans += i
        elif i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
        else:
            ans += i
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        if i%3==0 and i%5==0:
            sum += 0
        elif i%3==0:
            sum += 0
        elif i%5==0:
            sum += 0
        else:
            sum += i
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        if i%3==0 and i%5==0:
            continue
        elif i%3==0 or i%5==0:
            continue
        else:
            sum += i
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        if i % 3 == 0:
            continue
        if i % 5 == 0:
            continue
        ans += i
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    if N < 3:
        print(0)
        return
    if N < 5:
        print(3)
        return
    if N < 15:
        print(8)
        return
    if N < 10

=======
Suggestion 8

def main():
    N = int(input())
    print(sum([i for i in range(1, N + 1) if i % 3 != 0 and i % 5 != 0]) + 2 * sum([i for i in range(1, N + 1) if i % 3 == 0 and i % 5 != 0]) + 4 * sum([i for i in range(1, N + 1) if i % 3 != 0 and i % 5 == 0]) + 15 * sum([i for i in range(1, N + 1) if i % 3 == 0 and i % 5 == 0]))

=======
Suggestion 9

def main():
    N = int(input())
    print(sum([i if i%3!=0 and i%5!=0 else 0 for i in range(1,N+1)]) + 3*sum([i if i%3==0 and i%5!=0 else 0 for i in range(1,N+1)]) + 5*sum([i if i%3!=0 and i%5==0 else 0 for i in range(1,N+1)]))

=======
Suggestion 10

def main():
    N = int(input())
    print(solve(N))
