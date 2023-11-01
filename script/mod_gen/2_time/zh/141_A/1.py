def weather():
    weather = input('请输入今天的天气：')
    if weather == 'Sunny':
        print('明天是Cloudy')
    elif weather == 'Cloudy':
        print('明天是Rainy')
    else:
        print('明天是Sunny')

if __name__ == '__main__':
    weather()