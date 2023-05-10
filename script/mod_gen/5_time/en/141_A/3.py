def weather(s):
    if s == "Sunny":
        return "Cloudy"
    elif s == "Cloudy":
        return "Rainy"
    elif s == "Rainy":
        return "Sunny"
    else:
        return "Error"
s = input()
print(weather(s))

if __name__ == '__main__':
    weather()