def calc_deposit_year(deposit):
    year = 0
    while deposit < X:
        deposit += deposit//100
        year += 1
    return year
