def next_weather(weather):
    if weather == "晴天":
        return "阴天"
    elif weather == "阴天":
        return "雨天"
    else:
        return "晴天"
weather = input()
print(next_weather(weather))
