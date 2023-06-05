def century(year):
    # Finish this :)
    if year%100 == 0:
        return year//100
    else:
        return year//100 +1
print(century(2021))
print(century(200))
