def get_snow_cover(a,b):
    #a = number of meters the west tower is not covered with snow
    #b = number of meters the east tower is not covered with snow
    #return number of meters the snow cover is deep
    return b - a - 1
