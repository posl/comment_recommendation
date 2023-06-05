def next_weather(weather):
    if weather == '晴天':
        return '阴天'
    elif weather == '阴天':
        return '雨天'
    elif weather == '雨天':
        return '晴天'
    else:
        return '输入错误'
