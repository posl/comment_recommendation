def next_sport_year(year):
    while True:
        year += 1
        if year % 4 == 2:
            return year
