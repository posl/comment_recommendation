def main():
    weather = ['Sunny', 'Cloudy', 'Rainy']
    today = input()
    print(weather[(weather.index(today) + 1) % 3])

if __name__ == '__main__':
    main()