Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)

=======
Suggestion 2

def main():
    N = int(input())
    if N % 100 == 0:
        print(N // 100)
    else:
        print(N // 100 + 1)

=======
Suggestion 3

def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

n = int(input())
print(century(n))

=======
Suggestion 4

def main():
    n = int(input())
    if n % 100 == 0:
        print(int(n / 100))
    else:
        print(int(n / 100 + 1))

=======
Suggestion 5

def main():
    n = int(input())
    ans = n // 100
    if n % 100 != 0:
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = N // 100
    if N % 100 != 0:
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    print((n+99)//100)

=======
Suggestion 8

def main():
    n = int(input())
    print((n + 99) // 100)
    return

=======
Suggestion 9

def main():
    N = int(input())
    print((N-1)//100 + 1)

=======
Suggestion 10

def century(year):
    return (year + 99) // 100
