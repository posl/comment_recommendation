def main():
    S = input()
    weather = ["Sunny", "Cloudy", "Rainy"]
    index = weather.index(S)
    print(weather[(index+1)%3])
