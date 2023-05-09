def weather():
    today = input()
    if today == 'Sunny':
        print('Cloudy')
    elif today == 'Cloudy':
        print('Rainy')
    elif today == 'Rainy':
        print('Sunny')
    else:
        print('Invalid Input')
