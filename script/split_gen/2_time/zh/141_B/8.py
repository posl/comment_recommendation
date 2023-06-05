def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    elif s == "雨天":
        return "晴天"
    else:
        return "输入格式错误"
