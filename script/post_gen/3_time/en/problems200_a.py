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

def main():
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)

main()

=======
Suggestion 3

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 4

def century_from_year(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

=======
Suggestion 5

def main():
    N = int(input())
    print((N + 99) // 100)

=======
Suggestion 6

def century(year):
    century = year//100
    if year%100 != 0:
        century += 1
    return century

=======
Suggestion 7

def century(year):
    return (year + 99) // 100
