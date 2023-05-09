def weather_prediction():
    weather = input()
    if weather == 'Sunny':
        return 'Cloudy'
    elif weather == 'Cloudy':
        return 'Rainy'
    else:
        return 'Sunny'
print(weather_prediction())
