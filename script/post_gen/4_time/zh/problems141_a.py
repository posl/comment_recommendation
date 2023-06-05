Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = raw_input()
    if s == 'Sunny':
        print 'Cloudy'
    elif s == 'Cloudy':
        print 'Rainy'
    elif s == 'Rainy':
        print 'Sunny'
    else:
        print 'error'

=======
Suggestion 2

def weatherPredict(s):
    if s == '晴天':
        print('阴天')
    elif s == '阴天':
        print('雨天')
    else:
        print('晴天')

=======
Suggestion 3

def weather():
    weather_dict = {'晴天':'阴天', '阴天':'雨天', '雨天':'晴天'}
    weather = input()
    print(weather_dict[weather])

weather()

=======
Suggestion 4

def next_weather(weather):
    if weather == "晴天":
        return "阴天"
    elif weather == "阴天":
        return "雨天"
    else:
        return "晴天"

weather = input()
print(next_weather(weather))

=======
Suggestion 5

def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    elif s == "雨天":
        return "晴天"

=======
Suggestion 6

def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    else:
        return "晴天"

=======
Suggestion 7

def main():
    weather = input()
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    else:
        print("晴天")

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

def next_weather(weather):
    if weather == '晴天':
        return '阴天'
    elif weather == '阴天':
        return '雨天'
    elif weather == '雨天':
        return '晴天'
    else:
        return '输入错误'
