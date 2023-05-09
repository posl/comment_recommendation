Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

year = int(input())
print(century(year))

=======
Suggestion 2

def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

n = int(input())
print(century(n))

=======
Suggestion 3

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 4

def main():
    N = int(input())
    if N % 100 == 0:
        print(N//100)
    else:
        print(N//100 + 1)

=======
Suggestion 5

def century(year):
    century = year // 100
    if year % 100 == 0:
        return century
    else:
        return century + 1

=======
Suggestion 6

def century(year):
    if year%100 == 0:
        return year//100
    else:
        return year//100 + 1

print(century(int(input())))

=======
Suggestion 7

def century(year):
    if (year % 100 == 0):
        return (year // 100)
    else:
        return (year // 100) + 1

=======
Suggestion 8

def century(year):
    return (year+99)//100

year = int(input())
print(century(year))

=======
Suggestion 9

def main():
    N = int(input())
    print((N-1)//100+1)
