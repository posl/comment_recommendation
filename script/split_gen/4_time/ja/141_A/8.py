def main():
    s = input()
    weathers = ["Sunny", "Cloudy", "Rainy"]
    idx = weathers.index(s)
    print(weathers[(idx+1)%3])
