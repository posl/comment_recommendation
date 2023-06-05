def getCentury(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century
year = int(input())
print(getCentury(year))
