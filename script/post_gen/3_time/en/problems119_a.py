Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 2

def main():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 3

def main():
    date = input()
    if date <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 4

def main():
    date = input()
    if date <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    s = input()
    if s <= '2019/04/30':
        print('Heisei')
    else:
        print('TBD')
main()

=======
Suggestion 6

def main():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) > 2019:
        print("TBD")
    else:
        if int(S[1]) < 4:
            print("Heisei")
        elif int(S[1]) > 4:
            print("TBD")
        else:
            if int(S[2]) <= 30:
                print("Heisei")
            else:
                print("TBD")

=======
Suggestion 7

def main():
    s = input()
    if int(s[5:7]) <= 4:
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 8

def main():
    date = input()
    year, month, day = date.split('/')
    if month == '04' and day == '30':
        print('Heisei')
    elif month == '04' and day < '30':
        print('Heisei')
    elif month < '04':
        print('Heisei')
    else:
        print('TBD')
