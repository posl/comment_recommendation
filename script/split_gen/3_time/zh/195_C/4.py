def get_comma_count(num):
    if num < 1000:
        return 0
    else:
        return (num//1000)*3 + get_comma_count(num%1000)
