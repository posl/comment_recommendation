def weather():
    weather = input("请输入天气：")
    if weather == "Sunny":
        print("Cloudy")
    elif weather == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

if __name__ == '__main__':
    weather()