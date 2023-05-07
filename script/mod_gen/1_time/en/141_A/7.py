def weather_prediction(weather):
    weather_list = ["Sunny", "Cloudy", "Rainy"]
    weather_index = weather_list.index(weather)
    if weather_index == 2:
        return weather_list[0]
    else:
        return weather_list[weather_index + 1]
weather = input()
print(weather_prediction(weather))

if __name__ == '__main__':
    weather_prediction()