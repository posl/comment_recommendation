def main():
    S = input()
    weather = ["Sunny", "Cloudy", "Rainy"]
    print(weather[(weather.index(S) + 1) % 3])

if __name__ == '__main__':
    main()