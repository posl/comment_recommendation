def weather_prediction():
    n = int(input())
    s = input()
    if s[n-1] == 'o':
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    weather_prediction()