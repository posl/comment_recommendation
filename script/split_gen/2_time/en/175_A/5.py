def main():
    S = input()
    max_rain = 0
    rain = 0
    for i in range(3):
        if S[i] == 'R':
            rain += 1
            if rain > max_rain:
                max_rain = rain
        else:
            rain = 0
    print(max_rain)
