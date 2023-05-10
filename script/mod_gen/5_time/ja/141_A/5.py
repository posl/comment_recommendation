def get_forecast(s):
    if s == "Sunny":
        return "Cloudy"
    elif s == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"

if __name__ == '__main__':
    get_forecast()