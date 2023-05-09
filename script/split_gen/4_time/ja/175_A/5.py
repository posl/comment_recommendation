def main():
    s = input()
    max_rain = 0
    rain = 0
    for i in range(3):
        if s[i] == "R":
            rain += 1
        else:
            max_rain = max(max_rain, rain)
            rain = 0
    max_rain = max(max_rain, rain)
    print(max_rain)
