def isSunny(day, weather):
    if weather[day-1] == 'o':
        return True
    else:
        return False

if __name__ == '__main__':
    isSunny()