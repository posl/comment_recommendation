Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    century = N // 100
    if N % 100 == 0:
        print(century)
    else:
        print(century + 1)

=======
Suggestion 2

def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 3

def centuryFromYear(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1

=======
Suggestion 4

def main():
    N = int(input())
    print(N // 100 + 1 if N % 100 != 0 else N // 100)

=======
Suggestion 5

def main():
    N = int(input())
    print((N + 99) // 100)

=======
Suggestion 6

def main():
    n = int(input())
    print((n + 99) // 100)

=======
Suggestion 7

def main():
    n = int(input())
    print(n // 100 + 1)

=======
Suggestion 8

def century_from_year(year):
    # 1 ≦ N ≦ 3000
    if year < 1 or year > 3000:
        return -1

    return (year + 99) // 100
