def main():
    # 晴天，阴天，雨天，晴天，阴天，雨天，......
    weather = ['晴天', '阴天', '雨天']
    # 输入
    today_weather = input()
    # 打印输出
    print(weather[(weather.index(today_weather) + 1) % 3])
