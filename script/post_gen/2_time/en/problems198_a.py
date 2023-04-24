Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(int(n*(n-1)/2))

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += i
    print(ans)

=======
Suggestion 3

def divide_sweets(n):
    if n == 1:
        return 0
    elif n%2 == 0:
        return n//2 - 1
    else:
        return n//2

=======
Suggestion 4

def main():
    n = int(input())
    print(n-1)

=======
Suggestion 5

def main():
    N = int(input())
    print(N-1)

=======
Suggestion 6

def main():
    n = int(input())
    print(int((n-1)*n/2))

=======
Suggestion 7

def main():
    N = int(input())
    result = N - 1
    print(result)
