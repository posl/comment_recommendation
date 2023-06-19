def weather(S):
    if S == "晴天":
        return "阴天"
    elif S == "阴天":
        return "雨天"
    elif S == "雨天":
        return "晴天"

if __name__ == '__main__':
    weather()