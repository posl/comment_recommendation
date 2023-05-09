def weather():
    w = input()
    if w == 'Sunny':
        print('Cloudy')
    elif w == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')

if __name__ == '__main__':
    weather()