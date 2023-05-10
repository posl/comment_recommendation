def checkWeatherForecast():
    N = int(input())
    S = input()
    if S[N-1] == 'o':
        return "Yes"
    else:
        return "No"
