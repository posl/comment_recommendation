def main():
    input_line = input()
    input_line_split = input_line.split()
    hour = int(input_line_split[0])
    minute = int(input_line_split[1])
    while True:
        minute += 1
        if minute >= 60:
            minute = 0
            hour += 1
            if hour >= 24:
                hour = 0
        minute_1 = minute % 10
        minute_10 = int(minute / 10)
        hour_1 = hour % 10
        hour_10 = int(hour / 10)
        if minute_1 == hour_10 and minute_10 == hour_1:
            print(hour, minute)
            break

if __name__ == '__main__':
    main()