def main():
    weather = input()
    if weather == "Sunny":
        print("Cloudy")
    elif weather == "Cloudy":
        print("Rainy")
    elif weather == "Rainy":
        print("Sunny")
    else:
        print("Error")

if __name__ == '__main__':
    main()