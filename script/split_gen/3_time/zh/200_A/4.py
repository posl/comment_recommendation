def century(year):
    return (year-1)//100+1
year = int(input())
print(century(year))
