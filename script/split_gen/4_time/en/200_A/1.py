def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
year = int(input())
print(century(year))
