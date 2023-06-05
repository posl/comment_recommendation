def main():
    weather = input()
    rain_day = 0
    max_rain_days = 0
    for i in range(3):
        if weather[i] == "R":
            rain_day += 1
            if rain_day > max_rain_days:
                max_rain_days = rain_day
        else:
            rain_day = 0
    print(max_rain_days)

if __name__ == '__main__':
    main()