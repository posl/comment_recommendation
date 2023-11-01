def weather_tomorrow(weather):
    if weather == 'Sunny':
        return 'Cloudy'
    elif weather == 'Cloudy':
        return 'Rainy'
    else:
        return 'Sunny'

if __name__ == '__main__':
    weather_tomorrow()