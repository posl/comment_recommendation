def get_next_year(year):
    while True:
        if year % 4 == 2:
            return year
        year += 1
