def judge(year, month, day):
    if year > 2019:
        return "TBD"
    elif year < 2019:
        return "Heisei"
    elif month > 4:
        return "TBD"
    elif month < 4:
        return "Heisei"
    elif day > 30:
        return "TBD"
    else:
        return "Heisei"
year, month, day = map(int, input().split("/"))
print(judge(year, month, day))
