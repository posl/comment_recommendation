def main():
    weather = ['晴天', '阴天', '雨天']
    S = input()
    print(weather[(weather.index(S) + 1) % 3])
