def main():
    k = int(input())
    hour, minute = divmod(k, 60)
    hour = hour + 21
    minute = minute
    if hour > 23:
        hour = hour - 24
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)
    print(hour + ":" + minute)

if __name__ == '__main__':
    main()