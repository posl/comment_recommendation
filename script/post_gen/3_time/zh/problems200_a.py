Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def century(N):
    return (N+99)//100

=======
Suggestion 2

def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 3

def main():
    year = input("请输入年份：")
    year = int(year)
    if year % 100 == 0:
        year = year // 100
    else:
        year = year // 100 + 1
    print(year)

=======
Suggestion 4

def century(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

=======
Suggestion 5

def century(year):
    return (year-1)//100+1

year = int(input())
print(century(year))

=======
Suggestion 6

def main():
    N = int(input())
    print(int((N+99)/100))

=======
Suggestion 7

def getCentury(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

year = int(input())
print(getCentury(year))

=======
Suggestion 8

def problem200_a():
    n = int(input())
    print((n + 99) // 100)

=======
Suggestion 9

def problems200_a():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)

problems200_a()
