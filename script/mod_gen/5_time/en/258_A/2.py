def main():
    K = int(input())
    hour = 21
    minute = 0
    minute += K
    if minute >= 60:
        minute -= 60
        hour += 1
    print(str(hour).zfill(2) + ":" + str(minute).zfill(2))

if __name__ == '__main__':
    main()