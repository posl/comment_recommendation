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
