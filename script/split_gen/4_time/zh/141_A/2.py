def weather():
    weather_dict = {'晴天':'阴天', '阴天':'雨天', '雨天':'晴天'}
    weather = input()
    print(weather_dict[weather])
weather()
