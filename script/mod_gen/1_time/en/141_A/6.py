def weather_prediction(weather_today):
    if weather_today == "Sunny":
        return "Cloudy"
    elif weather_today == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"

if __name__ == '__main__':
    weather_prediction()