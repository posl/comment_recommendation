def century_from_year(year):
    # 1 ≦ N ≦ 3000
    if year < 1 or year > 3000:
        return -1
    return (year + 99) // 100
