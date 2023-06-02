Synthesizing 10/10 solutions

=======
Suggestion 1

def weather(s):
    if s == "晴天":
        return "阴天"
    elif s == "阴天":
        return "雨天"
    else:
        return "晴天"

=======
Suggestion 2

def main():
    weather = ['晴天', '阴天', '雨天']
    S = input()
    print(weather[(weather.index(S) + 1) % 3])

=======
Suggestion 3

def main():
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    elif weather == '雨天':
        print('晴天')

=======
Suggestion 4

def main():
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
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    else:
        print('晴天')

=======
Suggestion 6

def weather(S):
    if S == "晴天":
        return "阴天"
    elif S == "阴天":
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
    if weather == "晴天":
        print("阴天")
    elif weather == "阴天":
        print("雨天")
    elif weather == "雨天":
        print("晴天")

=======
Suggestion 9

def weather():
    weather = input()
    if weather == '晴天':
        print('阴天')
    elif weather == '阴天':
        print('雨天')
    elif weather == '雨天':
        print('晴天')
    else:
        print('Error')

weather()

=======
Suggestion 10

def main():
    s = input()
    if s == '晴天':
        print('阴天')
    elif s == '阴天':
        print('雨天')
    else:
        print('晴天')
