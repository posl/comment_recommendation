Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    weather = input()
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    elif weather == "雨天":
        print("晴天")
    else:
        print("输入错误")

=======
Suggestion 2

def main():
    str = input()
    if str == '晴天':
        print('阴天')
    elif str == '阴天':
        print('雨天')
    else:
        print('晴天')

=======
Suggestion 3

def main():
    weathers = ["晴天", "阴天", "雨天"]
    today_weather = input()
    today_index = weathers.index(today_weather)
    tomorrow_index = (today_index + 1) % 3
    print(weathers[tomorrow_index])

=======
Suggestion 4

def weather():
    s = input()
    if s == "晴天":
        print("阴天")
    elif s == "阴天":
        print("雨天")
    else:
        print("晴天")

=======
Suggestion 5

def main():
    s = input()
    if s == "晴天":
        print("阴天")
    elif s == "阴天":
        print("雨天")
    else:
        print("晴天")

=======
Suggestion 6

def weather():
    weather_today = input()
    if weather_today == '晴天':
        print('阴天')
    elif weather_today == '阴天':
        print('雨天')
    else:
        print('晴天')
weather()

=======
Suggestion 7

def main():
    weather = input()
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    elif weather == "雨天":
        print("晴天")
    else:
        print("输入有误")

=======
Suggestion 8

def main():
    weather = input()
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    else:
        print("晴天")

=======
Suggestion 9

def main():
    str = input()
    if str == '晴天':
        print('阴天')
    elif str == '阴天':
        print('雨天')
    elif str == '雨天':
        print('晴天')

=======
Suggestion 10

def weather(s):
    if s == '晴天':
        return '阴天'
    elif s == '阴天':
        return '雨天'
    else:
        return '晴天'
