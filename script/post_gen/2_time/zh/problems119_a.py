Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    s1 = s.split('/')
    if int(s1[0]) < 2019:
        print('Heisei')
    elif int(s1

=======
Suggestion 2

def main():
    date = input()
    if date <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 3

def main():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 4

def main():
    S = input()
    year, month, day = S.split('/')
    if int(year) < 2019:
        print('Heisei')

=======
Suggestion 5

def main():
    date = input()
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    i

=======
Suggestion 6

def main():
    s = input()
    y, m, d = map(int, s.split('/'))
    if y < 2019:
        print('Heisei')
    elif

=======
Suggestion 7

def main():
    S = input()
    a = S.split("/")
    if int(a[0]) < 2019:
        print("Heisei")
    elif int(a[0]

=======
Suggestion 8

def main():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 9

def is_heisei(s):
    year, month, day = map(int, s.split("/"))
    if year < 2019:
        return True
    elif ye
