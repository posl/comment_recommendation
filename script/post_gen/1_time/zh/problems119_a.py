Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10]

=======
Suggestion 2

def main():
    date = input()
    year, month, day = date.split("/")
    if int(year) < 2019:
        print

=======
Suggestion 3

def main():
    S = input()
    year, month, day = map(int, S.split('/'))
    if year < 2019:
        print("

=======
Suggestion 4

def main():
    s = input()
    s = s.split("/")
    if int(s[0]) < 2019:
        print("Heisei")
    elif int

=======
Suggestion 5

def main():
    S = input()
    year, month, day = S.split('/')
    year = int(year)
    month = int(month)

=======
Suggestion 6

def main():
    s = input()
    y, m, d = map(int, s.split("/"))
    if y <= 2019 and m <= 4 and d <= 30:

=======
Suggestion 7

def main():
    s = input()
    year, month, day = map(int, s.split("/"))
    if year < 2019:
        print("

=======
Suggestion 8

def main():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 9

def main():
    S = input()
    s = S.split("/")
    if int(s[0]) < 2019:
        print("Heisei")
    elif int

=======
Suggestion 10

def main():
    date = input()
    year, month, day = date.split('/')
    year = int(year)
    month = int(month)
    day = int
