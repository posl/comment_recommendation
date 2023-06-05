def main():
    hour, minute = map(int, input().split())
    while True:
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0
        if hour // 10 == minute % 10 and hour % 10 == minute // 10:
            break
    print("{:0>2}:{:0>2}".format(hour, minute))

if __name__ == '__main__':
    main()