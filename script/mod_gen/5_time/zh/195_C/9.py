def comma_count(n):
    if n < 1000:
        return 0
    else:
        return int((n-1000)/1000) + 1 + comma_count(int((n-1000)/1000)*1000 + 999)
print(comma_count(int(input())))
