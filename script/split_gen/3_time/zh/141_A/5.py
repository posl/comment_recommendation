def weather():
    weather_today = input()
    if weather_today == '晴天':
        print('阴天')
    elif weather_today == '阴天':
        print('雨天')
    else:
        print('晴天')
weather()
