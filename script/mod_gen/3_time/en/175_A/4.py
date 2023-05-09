def main():
    weather = input()
    rainy_days = 0
    max_rainy_days = 0
    for day in weather:
        if day == "R":
            rainy_days += 1
        else:
            rainy_days = 0
        if rainy_days > max_rainy_days:
            max_rainy_days = rainy_days
    print(max_rainy_days)

if __name__ == '__main__':
    main()