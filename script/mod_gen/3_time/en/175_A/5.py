def max_rainy_days(s):
    rainy_days = 0
    max_rainy_days = 0
    for i in range(len(s)):
        if s[i] == "R":
            rainy_days += 1
        else:
            rainy_days = 0
        if rainy_days > max_rainy_days:
            max_rainy_days = rainy_days
    return max_rainy_days

if __name__ == '__main__':
    max_rainy_days()