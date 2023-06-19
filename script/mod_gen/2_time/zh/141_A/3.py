def get_next_weather(weather):
    if weather == '晴天':
        return '阴天'
    elif weather == '阴天':
        return '雨天'
    else:
        return '晴天'

if __name__ == '__main__':
    get_next_weather()