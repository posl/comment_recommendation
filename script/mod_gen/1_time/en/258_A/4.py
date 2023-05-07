def main():
    k = int(input())
    hour = 21
    minute = 0
    total = k + minute
    hour += total // 60
    minute = total % 60
    print(str(hour) + ":" + str(minute).zfill(2))

if __name__ == '__main__':
    main()