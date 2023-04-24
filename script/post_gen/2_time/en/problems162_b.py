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
    for i in range(1, N + 1):
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
        if i % 3 != 0 and i % 5 != 0:
            sum += i
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        ans += i
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i%3 != 0 and i%5 != 0:
            sum += i
    print(sum)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
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
    sum = 0
    for i in range(1,N+1):
        if (i % 3 != 0) and (i % 5 != 0):
            sum += i
    print(sum)
main()

=======
Suggestion 8

def fizzbuzz(N):
    # Write your code here
    return 0
