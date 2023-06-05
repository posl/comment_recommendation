def main():
    S = input()
    #print(S)
    rain = 0
    max_rain = 0
    for i in range(len(S)):
        #print(S[i])
        if S[i] == 'S':
            rain = 0
        elif S[i] == 'R':
            rain += 1
        if max_rain < rain:
            max_rain = rain
    print(max_rain)

if __name__ == '__main__':
    main()