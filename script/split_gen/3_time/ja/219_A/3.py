def main():
    x = int(input())
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    elif 90 <= x <= 100:
        print('expert')