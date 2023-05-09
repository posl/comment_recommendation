def main():
    K = int(input())
    hours = 21
    minutes = 0
    minutes += K % 60
    hours += int(K / 60)
    if minutes >= 60:
        minutes = minutes % 60
        hours += 1
    print(str(hours) + ":" + str(minutes).zfill(2))

if __name__ == '__main__':
    main()