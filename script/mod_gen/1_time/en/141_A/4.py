def weather(S):
    if S == "Sunny":
        return "Cloudy"
    elif S == "Cloudy":
        return "Rainy"
    elif S == "Rainy":
        return "Sunny"

if __name__ == '__main__':
    weather()