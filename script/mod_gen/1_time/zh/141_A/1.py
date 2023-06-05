def weather():
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    elif weather == '雨天':
        print('晴天')

if __name__ == '__main__':
    weather()