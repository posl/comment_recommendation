def main():
    S = input()
    rain = 0
    max_rain = 0
    for i in range(3):
        if S[i] == "R":
            rain += 1
        else:
            rain = 0
        if max_rain < rain:
            max_rain = rain
    print(max_rain)

if __name__ == '__main__':
    main()