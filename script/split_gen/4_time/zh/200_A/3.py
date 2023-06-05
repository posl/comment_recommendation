def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
print(century_from_year(2021))
print(century_from_year(200))
print(century_from_year(1900))
print(century_from_year(3000))
print(century_from_year(3001))
print(century_from_year(0))
print(century_from_year(1))
print(century_from_year(99))
print(century_from_year(100))
print(century_from_year(101))
print(century_from_year(199))
print(century_from_year(200))
print(century_from_year(201))
print(century_from_year(899))
print(century_from_year(900))
print(century_from_year(901))
print(century_from_year(999))
print(century_from_year(1000))
print(century_from_year(1001))
print(century_from_year(9999))
print(century_from_year(10000))
print(century_from_year(10001))
