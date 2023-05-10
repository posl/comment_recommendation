def century(year):
    return (year+99)//100
year = int(input())
print(century(year))

if __name__ == '__main__':
    century()