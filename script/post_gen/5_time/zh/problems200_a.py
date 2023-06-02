Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    century = n // 100
    if n % 100 != 0:
        century += 1
    print(century)

=======
Suggestion 2

def main():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)

=======
Suggestion 3

def century(year):
    if year%100 == 0:
        return int(year/100)
    else:
        return int(year/100)+1

=======
Suggestion 4

def get_century(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

=======
Suggestion 5

def main():
    N = int(input())
    print(N%100)
    if N%100 == 0:
        print(N//100)
    else:
        print(N//100 + 1)

=======
Suggestion 6

def main():
    N = int(input())
    print((N+99)//100)

=======
Suggestion 7

def century(year):
    return (year + 99) // 100

=======
Suggestion 8

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

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

print(century(int(input())))
