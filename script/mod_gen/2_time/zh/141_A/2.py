def main():
    # 读取输入
    weather = input()
    # 定义天气列表
    weather_list = ['晴天', '阴天', '雨天']
    # 通过列表下标获取天气
    print(weather_list[(weather_list.index(weather) + 1) % 3])

if __name__ == '__main__':
    main()