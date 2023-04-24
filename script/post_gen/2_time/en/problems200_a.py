Synthesizing 10/10 solutions (Duplicates hidden)

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

def century(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

year = int(input())
print(century(year))

=======
Suggestion 3

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 4

def century(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

=======
Suggestion 5

def century(n):
    if n % 100 == 0:
        return int(n/100)
    else:
        return int(n/100) + 1

=======
Suggestion 6

def century(n):
    if n%100==0:
        return n//100
    else:
        return n//100+1

=======
Suggestion 7

def main():
    N = int(input())
    print((N-1)//100+1)
