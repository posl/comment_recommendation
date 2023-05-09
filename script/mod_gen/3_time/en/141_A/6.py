def predict_weather(weather):
    if weather == "Sunny":
        return "Cloudy"
    elif weather == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"

if __name__ == '__main__':
    predict_weather()