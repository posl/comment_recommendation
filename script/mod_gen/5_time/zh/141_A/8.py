def weather(S):
    if S == 'Sunny':
        return 'Cloudy'
    elif S == 'Cloudy':
        return 'Rainy'
    else:
        return 'Sunny'

if __name__ == '__main__':
    weather()