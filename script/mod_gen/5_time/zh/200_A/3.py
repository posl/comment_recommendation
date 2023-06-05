def get_century(year):
    century = year // 100
    if year % 100 != 0:
        century += 1
    return century

if __name__ == '__main__':
    get_century()