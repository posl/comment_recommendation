def main():
    weather = ['Sunny', 'Cloudy', 'Rainy']
    today = input()
    print(weather[(weather.index(today) + 1) % 3])
