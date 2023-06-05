def main():
    weathers = ["晴天", "阴天", "雨天"]
    today_weather = input()
    today_index = weathers.index(today_weather)
    tomorrow_index = (today_index + 1) % 3
    print(weathers[tomorrow_index])

if __name__ == '__main__':
    main()