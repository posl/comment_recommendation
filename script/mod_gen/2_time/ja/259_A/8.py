def calc_height(year, start_year, start_height, grow_height):
    if year == start_year:
        return start_height
    elif year < start_year:
        return 0
    else:
        return calc_height(year-1, start_year, start_height, grow_height) + grow_height

if __name__ == '__main__':
    calc_height()