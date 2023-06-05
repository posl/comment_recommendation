def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    elif s == "雨天":
        return "晴天"

if __name__ == '__main__':
    weather()