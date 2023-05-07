def main():
    k = int(input())
    hour = 21
    minute = 0
    hour = (k + hour) % 24
    minute = k % 60
    print(str(hour).zfill(2) + ':' + str(minute).zfill(2))

if __name__ == '__main__':
    main()