def get_weather(str):
    if str == "Sunny":
        return "Cloudy"
    elif str == "Cloudy":
        return "Rainy"
    elif str == "Rainy":
        return "Sunny"

if __name__ == '__main__':
    get_weather()