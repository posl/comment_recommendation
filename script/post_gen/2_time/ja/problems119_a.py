Synthesizing 9/10 solutions

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

def is_heisei(year, month, day):
    if year > 2019:
        return False
    elif year == 2019 and month > 4:
        return False
    elif year == 2019 and month == 4 and day > 30:
        return False
    return True

=======
Suggestion 3

def judge_heisei(year, month, day):
    if year > 2019:
        return False
    elif year == 2019:
        if month > 4:
            return False
        elif month == 4:
            if day > 30:
                return False
    return True

=======
Suggestion 4

def judge(year,month,day):
    if year < 2019:
        return True
    elif year > 2019:
        return False
    else:
        if month < 4:
            return True
        elif month > 4:
            return False
        else:
            if day <= 30:
                return True
            else:
                return False

=======
Suggestion 5

def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(m) < 4:
        print('Heisei')
    elif int(d) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 6

def judge(s):
    year, month, day = map(int, s.split('/'))
    if year > 2019:
        return 'TBD'
    elif year == 2019 and month > 4:
        return 'TBD'
    elif year == 2019 and month == 4 and day > 30:
        return 'TBD'
    else:
        return 'Heisei'

s = input()
print(judge(s))

=======
Suggestion 7

def judge():
    s = input()
    year = int(s[0:4])
    month = int(s[5:7])
    day = int(s[8:10])
    if year < 2019:
        print('Heisei')
    elif year == 2019:
        if month < 4:
            print('Heisei')
        elif month == 4:
            if day <= 30:
                print('Heisei')
            else:
                print('TBD')
        else:
            print('TBD')
    else:
        print('TBD')

judge()

=======
Suggestion 8

def judge(input_date):
    judge_date = '2019/04/30'
    if input_date <= judge_date:
        return 'Heisei'
    else:
        return 'TBD'

=======
Suggestion 9

def judge(date):
    if date <= 430:
        print("Heisei")
    else:
        print("TBD")
