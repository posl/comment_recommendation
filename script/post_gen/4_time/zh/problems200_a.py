Synthesizing 10/10 solutions

=======
Suggestion 1

def century_from_year(year):
    return (year - 1) // 100 + 1

=======
Suggestion 2

def century(N):
    return (N-1)//100+1

=======
Suggestion 3

def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

print(century(int(input())))

=======
Suggestion 4

def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

print(century_from_year(2021))
print(century_from_year(200))
print(century_from_year(1900))
print(century_from_year(3000))
print(century_from_year(3001))
print(century_from_year(0))
print(century_from_year(1))
print(century_from_year(99))
print(century_from_year(100))
print(century_from_year(101))
print(century_from_year(199))
print(century_from_year(200))
print(century_from_year(201))
print(century_from_year(899))
print(century_from_year(900))
print(century_from_year(901))
print(century_from_year(999))
print(century_from_year(1000))
print(century_from_year(1001))
print(century_from_year(9999))
print(century_from_year(10000))
print(century_from_year(10001))

=======
Suggestion 5

def century(year):
    # Finish this :)
    if year%100 == 0:
        return year//100
    else:
        return year//100 +1

print(century(2021))
print(century(200))

=======
Suggestion 6

def main():
    N = int(input())
    if N % 100 == 0:
        century = N // 100
    else:
        century = N // 100 + 1
    print(century)

=======
Suggestion 7

def main():
    n = int(input())
    print((n+99)//100)

=======
Suggestion 8

def century_from_year(year):
    if year % 100 == 0:
        return int(year/100)
    else:
        return int(year/100)+1

=======
Suggestion 9

def getCentury(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 10

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
