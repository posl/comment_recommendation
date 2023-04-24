Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S == 'Sunny':
        print('Cloudy')
    elif S == 'Cloudy':
        print('Rainy')
    elif S == 'Rainy':
        print('Sunny')

=======
Suggestion 2

def main():
    S = input()
    if S == 'Sunny':
        print('Cloudy')
    elif S == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')

=======
Suggestion 3

def main():
    weather = input()
    if weather == 'Sunny':
        print('Cloudy')
    elif weather == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')

=======
Suggestion 4

def main():
    today = input()
    if today == 'Sunny':
        print('Cloudy')
    elif today == 'Cloudy':
        print('Rainy')
    elif today == 'Rainy':
        print('Sunny')

=======
Suggestion 5

def weather(S):
    if S == "Sunny":
        return "Cloudy"
    elif S == "Cloudy":
        return "Rainy"
    elif S == "Rainy":
        return "Sunny"

=======
Suggestion 6

def weather(s):
    if s == "Sunny":
        return "Cloudy"
    elif s == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"

=======
Suggestion 7

def weather_prediction(weather_today):
    if weather_today == "Sunny":
        return "Cloudy"
    elif weather_today == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"

=======
Suggestion 8

def weather_prediction(weather):
    weather_list = ["Sunny", "Cloudy", "Rainy"]
    weather_index = weather_list.index(weather)
    if weather_index == 2:
        return weather_list[0]
    else:
        return weather_list[weather_index + 1]

weather = input()
print(weather_prediction(weather))
