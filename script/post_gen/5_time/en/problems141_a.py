Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S == "Sunny":
        print("Cloudy")
    elif S == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

=======
Suggestion 2

def main():
    s = input()
    if s == "Sunny":
        print("Cloudy")
    elif s == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

=======
Suggestion 3

def main():
    weather = input()
    if weather == "Sunny":
        print("Cloudy")
    elif weather == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

=======
Suggestion 4

def weather(s):
    if s == "Sunny":
        return "Cloudy"
    elif s == "Cloudy":
        return "Rainy"
    elif s == "Rainy":
        return "Sunny"
    else:
        return "Error"

s = input()
print(weather(s))

=======
Suggestion 5

def weather_prediction(weather):
    if weather == 'Sunny':
        return 'Cloudy'
    elif weather == 'Cloudy':
        return 'Rainy'
    elif weather == 'Rainy':
        return 'Sunny'

=======
Suggestion 6

def weather_prediction(weather):
    if weather == 'Sunny':
        return 'Cloudy'
    elif weather == 'Cloudy':
        return 'Rainy'
    else:
        return 'Sunny'

=======
Suggestion 7

def weather_today():
    weather = input()
    if weather == 'Sunny':
        print('Cloudy')
    elif weather == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')

weather_today()

=======
Suggestion 8

def main():
    S = input()
    weather = ["Sunny", "Cloudy", "Rainy"]
    index = weather.index(S)
    print(weather[(index+1)%3])

=======
Suggestion 9

def main():
  s = input()
  weather = ['Sunny', 'Cloudy', 'Rainy']
  print(weather[(weather.index(s)+1)%3])
