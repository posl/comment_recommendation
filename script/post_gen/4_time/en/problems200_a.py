Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 100 == 0:
        print(N // 100)
    else:
        print(N // 100 + 1)

=======
Suggestion 2

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

year = int(input())
print(century(year))

=======
Suggestion 3

def main():
    year = int(input())
    if year % 100 == 0:
        print(year // 100)
    else:
        print(year // 100 + 1)

=======
Suggestion 4

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 5

def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

=======
Suggestion 6

def century(year):
    if year%100 == 0:
        return int(year/100)
    else:
        return int(year/100)+1

=======
Suggestion 7

def century(n):
    #divmod returns quotient and remainder
    q,r = divmod(n,100)
    if r == 0:
        return q
    else:
        return q+1

n = int(input())
print(century(n))
