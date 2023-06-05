def time_calculator(time):
    time = 21*60 + time
    hour = time // 60
    minute = time % 60
    return hour, minute

if __name__ == '__main__':
    time_calculator()