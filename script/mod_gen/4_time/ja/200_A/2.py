def getCentury(year):
    if year % 100 == 0:
        return int(year / 100)
    else:
        return int(year / 100) + 1

if __name__ == '__main__':
    getCentury()