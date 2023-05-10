def weather_today():
    weather = input()
    if weather == 'Sunny':
        print('Cloudy')
    elif weather == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')
weather_today()

if __name__ == '__main__':
    weather_today()