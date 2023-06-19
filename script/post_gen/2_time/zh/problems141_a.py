Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 晴天，阴天，雨天，晴天，阴天，雨天，......
    weather = ['晴天', '阴天', '雨天']
    # 输入
    today_weather = input()
    # 打印输出
    print(weather[(weather.index(today_weather) + 1) % 3])

=======
Suggestion 2

def weather_next(weather_today):
    if weather_today == '晴天':
        return '阴天'
    elif weather_today == '阴天':
        return '雨天'
    elif weather_today == '雨天':
        return '晴天'
    else:
        return 'Error'

=======
Suggestion 3

def main():
    # 读取输入
    weather = input()
    # 定义天气列表
    weather_list = ['晴天', '阴天', '雨天']
    # 通过列表下标获取天气
    print(weather_list[(weather_list.index(weather) + 1) % 3])

=======
Suggestion 4

def get_next_weather(weather):
    if weather == '晴天':
        return '阴天'
    elif weather == '阴天':
        return '雨天'
    else:
        return '晴天'

=======
Suggestion 5

def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    elif s == "雨天":
        return "晴天"
    else:
        return "error"

=======
Suggestion 6

def weather(S):
    if S == "晴天":
        return "阴天"
    elif S == "阴天":
        return "雨天"
    elif S == "雨天":
        return "晴天"

=======
Suggestion 7

def main():
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    elif weather == '雨天':
        print('晴天')

=======
Suggestion 8

def main():
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    else:
        print('晴天')

=======
Suggestion 9

def main():
    weather = input()
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    else:
        print("晴天")

=======
Suggestion 10

def weather_tomorrow(weather_today):
    if weather_today == "晴天":
        return "阴天"
    elif weather_today == "阴天":
        return "雨天"
    elif weather_today == "雨天":
        return "晴天"
